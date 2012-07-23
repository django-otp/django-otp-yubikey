from base64 import b64decode
from binascii import hexlify, unhexlify
from struct import pack

from django.db import models

from django_otp.models import Device
from django_otp.util import hex_validator, random_hex
from yubiotp.client import YubiClient10, YubiClient11, YubiClient20
from yubiotp.modhex import modhex
from yubiotp.otp import decode_otp

from .conf import settings


class YubikeyDevice(Device):
    """
    Represents a locally-verified YubiKey OTP device.

    .. attribute:: private_id

        The 6-byte private ID (hex-encoded).

    .. attribute:: key

        The 16-byte AES key shared with this YubiKey (hex-encoded).

    .. attribute:: session

        The non-volatile session counter most recently used by this device.

    .. attribute:: counter

        The volatile session usage counter most recently used by this device.
    """
    private_id = models.CharField(max_length=12,
        validators=[hex_validator(6)],
        default=lambda: random_hex(6),
        verbose_name="Private ID",
        help_text="The 6-byte private ID (hex-encoded)."
    )

    key = models.CharField(max_length=32,
        validators=[hex_validator(16)],
        default=lambda: random_hex(16),
        help_text="The 16-byte AES key shared with this YubiKey (hex-encoded)."
    )

    session = models.PositiveIntegerField(
        default=0,
        help_text="The non-volatile session counter most recently used by this device."
    )

    counter = models.PositiveIntegerField(
        default=0,
        help_text="The volatile session usage counter most recently used by this device."
    )

    class Meta(Device.Meta):
        verbose_name = "Local YubiKey device"

    def public_id(self):
        """
        The public ID of this device is the four-byte, big-endian,
        modhex-encoded primary key.
        """
        return modhex(pack('>I', self.id))
    public_id.short_description = 'Public Identity'
    public_id.admin_order_field = 'id'

    @property
    def bin_key(self):
        return unhexlify(self.key)

    def verify_token(self, token):
        try:
            public_id, otp = decode_otp(token, self.bin_key)
        except StandardError:
            return False

        if public_id != self.public_id():
            return False

        if hexlify(otp.uid) != self.private_id:
            return False

        if otp.session < self.session:
            return False

        if (otp.session == self.session) and (otp.counter <= self.counter):
            return False

        # All tests pass. Update the counters and return the good news.
        self.session = otp.session
        self.counter = otp.counter
        self.save()

        return True


class RemoteYubikeyDevice(Device):
    """
    Represents a YubiKey device that is to be verified with a remote validation
    service. By default, this uses Yubico's hosted validation service, but each
    device can be directed to any other validation service.

    .. attribute:: public_id

        The public identity of the YubiKey (modhex-encoded).

    .. attribute:: api_version

        The version of the validation API to use. (Default: '2.0')

    .. attribute:: api_id

        Your API ID. The server needs this to sign responsees. (Default: 1)

    .. attribute:: api_key

        Your base64-encoded API key, used to sign requests. This is optional
        but strongly recommended. (Default: ``None``)

    .. attribute:: use_ssl

        If ``True``, we'll use the HTTPS versions of the default URLs. Because
        :mod:`urllib2` does not verify certificates, this provides little
        benefit. (Default: ``False``).

    .. attribute:: param_sl

        The level of syncing required. See :class:`~yubiotp.client.YubiClient20`.

    .. attribute:: param_timeout

        The time to allow for syncing. See :class:`~yubiotp.client.YubiClient20`.

    .. attribute:: base_url

        The base URL of the verification service. Defaults to Yubico's hosted API.
    """
    API_VERSIONS = ['1.0', '1.1', '2.0']

    public_id = models.CharField(max_length=32,
        verbose_name="Public ID",
        help_text="The public identity of the YubiKey (modhex-encoded)."
    )

    api_version = models.CharField(max_length=8,
        choices=zip(API_VERSIONS, API_VERSIONS),
        default=settings.OTP_YUBIKEY_DEFAULT_API_VERSION,
        help_text="The version of the validation api to use."
    )

    api_id = models.IntegerField(
        default=settings.OTP_YUBIKEY_DEFAULT_API_ID,
        verbose_name="API ID",
        help_text="Your API ID."
    )

    api_key = models.CharField(max_length=64,
        blank=True,
        default=settings.OTP_YUBIKEY_DEFAULT_API_KEY,
        verbose_name="API key",
        help_text="Your base64-encoded API key."
    )

    use_ssl = models.BooleanField(
        default=False,
        verbose_name="Use SSL",
        help_text="Use HTTPS API URLs by default?"
    )

    param_sl = models.CharField(max_length=16,
        blank=True,
        default=None,
        verbose_name="SL",
        help_text="Level of server syncing required."
    )

    param_timeout = models.CharField(max_length=16,
        blank=True,
        default=None,
        verbose_name="Timeout",
        help_text="Sync timeout requested."
    )

    base_url = models.URLField(
        blank=True,
        default=settings.OTP_YUBIKEY_DEFAULT_BASE_URL,
        verbose_name="Base URL",
        help_text="The base URL of the verification service. Defaults to Yubico's hosted API."
    )

    class Meta(Device.Meta):
        verbose_name = "Remote YubiKey device"

    def verify_token(self, token):
        verified = False

        if token[:-32] == self.public_id:
            client = self._get_client()
            response = client.verify(token)
            verified = response.is_ok()

        return verified

    def _get_client(self):
        api_key = b64decode(self.api_key) or None

        if self.api_version == '2.0':
            client = YubiClient20(self.api_id, api_key, self.use_ssl, False, self.param_sl or None, self.param_timeout or None)
        elif self.api_version == '1.1':
            client = YubiClient11(self.api_id, api_key, self.use_ssl)
        else:
            client = YubiClient10(self.api_id, api_key, self.use_ssl)

        if self.base_url:
            client.base_url = self.base_url

        return client

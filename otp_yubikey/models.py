from binascii import hexlify, unhexlify
from struct import pack

from django.core.exceptions import ImproperlyConfigured
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
    private_id = models.CharField(max_length=12, validators=[hex_validator(6)], default=lambda: random_hex(6), help_text=u"The 6-byte private ID (hex-encoded).")
    key = models.CharField(max_length=32, validators=[hex_validator(16)], default=lambda: random_hex(16), help_text=u"The 16-byte AES key shared with this YubiKey (hex-encoded).")
    session = models.PositiveIntegerField(default=0, help_text=u"The non-volatile session counter most recently used by this device.")
    counter = models.PositiveIntegerField(default=0, help_text=u"The volatile session usage counter most recently used by this device.")

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

    .. attribute:: base_url

        The base URL of the verification service. Defaults to Yubico's hosted API.

    .. attribute:: public_id

        The public identity of the YubiKey (modhex-encoded).
    """
    base_url = models.URLField(blank=True, default=settings.OTP_YUBIKEY_DEFAULT_BASE_URL, help_text=u"The base URL of the verification service. Defaults to Yubico's hosted API.")
    public_id = models.CharField(max_length=32, help_text=u"The public identity of the YubiKey (modhex-encoded).")

    def verify_token(self, token):
        verified = False

        if token[:-32] == self.public_id:
            client = self._get_client()
            response = client.verify(token)
            verified = response.is_ok()

        return verified

    def _get_client(self):
        version = settings.OTP_YUBIKEY_PROTOCOL_VERSION
        api_id = settings.OTP_YUBIKEY_API_ID
        api_key = settings.OTP_YUBIKEY_API_KEY
        ssl = bool(settings.OTP_YUBIKEY_USE_SSL)

        if version == '1.0':
            client = YubiClient10(api_id, api_key, ssl)
        elif version == '1.1':
            client = YubiClient11(api_id, api_key, ssl)
        elif version == '2.0':
            sl = settings.OTP_YUBIKEY_SL
            timeout = settings.OTP_YUBIKEY_TIMEOUT

            client = YubiClient20(api_id, api_key, ssl, False, sl, timeout)
        else:
            raise ImproperlyConfigured("OTP_YUBIKEY_CLIENT_VERSION must be '1.0', '1.1', or '2.0'.")

        if self.base_url:
            client.base_url = self.base_url

        return client

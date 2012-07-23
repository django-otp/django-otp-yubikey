django-otp-yubikey
==================

.. include:: ../../README

Local Verification
------------------

.. autoclass:: otp_yubikey.models.YubikeyDevice
    :members:


Remote Verification
-------------------

.. autoclass:: otp_yubikey.models.RemoteYubikeyDevice
    :members:


RemoteYubikeyDevice Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every :class:`~otp_yubikey.models.RemoteYubikeyDevice` has a complete set of
configuration options for API access, allowing you to use different validation
services for different users. For convenience, there are a handful of settings
that you can use to populate these devices with default values.

All of the following settings are optional, however it is highly recommended
that you set and API ID/key. Without them, the security of the protocol is
severely compromised.

.. setting:: OTP_YUBIKEY_DEFAULT_API_ID

**OTP_YUBIKEY_DEFAULT_API_ID**

Default: ``1``

Your Yubico Web Service API ID. If you're using Yubico's service, you can get
one from https://upgrade.yubico.com/getapikey/.


.. setting:: OTP_YUBIKEY_DEFAULT_API_KEY

**OTP_YUBIKEY_DEFAULT_API_KEY**

Default: ``''``

Your Yubico Web Service API key. This is not technically required, but if it is
omitted, APIs requests and responses will not be digitally signed. If you're
using Yubico's service, you can get an API key from
https://upgrade.yubico.com/getapikey/.


.. setting:: OTP_YUBIKEY_DEFAULT_API_VERSION

**OTP_YUBIKEY_DEFAULT_API_VERSION**

Default: ``'2.0'``

The default version of the validation protocol to use. The default should be
fine unless you're validating against an old server that is confused by the
additional parameters.


.. setting:: OTP_YUBIKEY_DEFAULT_BASE_URL

**OTP_YUBIKEY_DEFAULT_BASE_URL**

Default: ``''``

The default base validation URL for new devices. Each device has its own base
URL; if left blank, we'll use Yubico's public service.


License
=======

.. include:: ../../LICENSE

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

All of the following settings are optional, however it is highly recommended
that you set and API ID/key. Without them, the security of the protocol is
severely compromised.

.. setting:: OTP_YUBIKEY_API_ID

**OTP_YUBIKEY_API_ID**

Default: ``1``

Your Yubico Web Service API ID. If you're using Yubico's service, you can get
one from https://upgrade.yubico.com/getapikey/.


.. setting:: OTP_YUBIKEY_API_KEY

**OTP_YUBIKEY_API_KEY**

Default: ``None``

Your Yubico Web Service API key. This is not technically required, but if it is
omitted, APIs requests and responses will not be digitally signed. If you're
using Yubico's service, you can get an API key from
https://upgrade.yubico.com/getapikey/.


.. setting:: OTP_YUBIKEY_DEFAULT_BASE_URL

**OTP_YUBIKEY_DEFAULT_BASE_URL**

Default: ``''``

The default base validation URL for new devices. Each device has its own base
URL; if left blank, we'll use Yubico's public service.


.. setting:: OTP_YUBIKEY_PROTOCOL_VERSION

**OTP_YUBIKEY_PROTOCOL_VERSION**

Default: ``'2.0'``

The version of the validation protocol to use. The default should be fine unless
you're validating against an old server that is confused by the additional
parameters.


.. setting:: OTP_YUBIKEY_SL

**OTP_YUBIKEY_SL**

Default: ``None``

The percentage of syncing required of the service. See `the protocol spec
<http://code.google.com/p/yubikey-val-server-php/wiki/ValidationProtocolV20>`_
for details.


.. setting:: OTP_YUBIKEY_TIMEOUT

**OTP_YUBIKEY_TIMEOUT**

Default: ``None``

Number of seconds to wait for sync responses. See `the protocol spec
<http://code.google.com/p/yubikey-val-server-php/wiki/ValidationProtocolV20>`_
for details.


.. setting:: OTP_YUBIKEY_USE_SSL

**OTP_YUBIKEY_USE_SSL**

Default: ``False``

If true, we will use Yubico's HTTPS urls by default. Note that because
:mod:`urllib2` does not verify HTTPS server certificates by default, this
provides little benefit.


License
=======

.. include:: ../../LICENSE

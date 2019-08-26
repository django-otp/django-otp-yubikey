django-otp-yubikey
==================

.. include:: ../../README.rst


Installation
------------

django-otp-yubikey can be installed via pip::

    pip install django-otp-yubikey


Once installed it should be added to INSTALLED_APPS after django_otp core::

    INSTALLED_APPS = [
        ...
        'django_otp',
        'django_otp.plugins.otp_totp',
        'django_otp.plugins.otp_hotp',
        'django_otp.plugins.otp_static',

        'otp_yubikey',
    ]


Local Verification
------------------

.. autoclass:: otp_yubikey.models.YubikeyDevice
    :members:


Remote Verification
-------------------

.. autoclass:: otp_yubikey.models.ValidationService
    :members:

.. autoclass:: otp_yubikey.models.RemoteYubikeyDevice
    :members:


Admin
-----

The following :class:`~django.contrib.admin.ModelAdmin` subclasses are
registered with the default admin site. We recommend their use with custom admin
sites as well:

.. autoclass:: otp_yubikey.admin.YubikeyDeviceAdmin

.. autoclass:: otp_yubikey.admin.ValidationServiceAdmin

.. autoclass:: otp_yubikey.admin.RemoteYubikeyDeviceAdmin


Changes
-------

:doc:`changes`


License
=======

.. include:: ../../LICENSE

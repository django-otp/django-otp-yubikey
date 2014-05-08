django-otp-yubikey
==================

.. include:: ../../README.rst

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

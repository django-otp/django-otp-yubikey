.. vim: ft=rst nospell tw=80

This is a django-otp plugin that handles `YubiKey
<http://www.yubico.com/yubikey>`_ devices using the Yubico OTP algorithm. This
includes two device definitions: one to verify YubiKey tokens locally and
another to verify them against a `web service
<http://www.yubico.com/yubicloud>`_.

See `django-otp <http://pypi.python.org/pypi/django-otp>`_ for more information
on the OTP framework.

This version is supported on Python 2.6, 2.7, and 3.3+; and Django >= 1.4.

.. warning::

    otp_yubikey now contains both South and Django migrations. If you're using
    South or upgrading to Django 1.7, please see the `upgrade notes`_ in the
    django-otp documentation first.

.. _upgrade notes: https://pythonhosted.org/django-otp/overview.html#upgrading

v1.0.0 - August 13, 2020 - Update supported Django verisons
--------------------------------------------------------------------------------

- Dropped support for Django < 2.2.

- Version bumped to align with the core django-otp project.


v0.6.0 - July 23, 2020 - Require TLS by default
-------------------------------------------------------------------------------

- Validation services require TLS by default. Python now (for some time)
  verifies server certificates.

- Removed vestigial Python 2 support. Updated the test matrix to match
  django-otp.


v0.5.2 - September 12, 2019 - Preliminary Django 3.0 support
------------------------------------------------------------

Removed dependencies on Python 2 compatibility shims in Django < 3.0.


v0.5.1 - August 26, 2019 - Housekeeping
---------------------------------------

Build, test, and documentation cleanup.


v0.5.0 - August 14, 2018 - Django 2.1 support
---------------------------------------------

- Drop support for Django < 1.11.


v0.4.2 - October 7, 2017 - Forward compatibility
------------------------------------------------

- Resolve deprecation warnings for forward compatibility.


v0.4.1 - August 29, 2017 - Default keys
---------------------------------------

- Fix `#25`_: make sure default keys are unicode values.

.. _#25: https://bitbucket.org/psagers/django-otp/issues/25/attributeerror-bytes-object-has-no


v0.4.0 - July 19, 2017 - Update support matrix
----------------------------------------------

- Drop support for versions of Django that are past EOL.


v0.3.5 - November 27, 2016 - Forward compatbility for Django 2.0
----------------------------------------------------------------

- Treat :attr:`~django.contrib.auth.models.User.is_authenticated` and
  :attr:`~django.contrib.auth.models.User.is_anonymous` as properties in Django
  1.10 and later.

- Add explict on_delete behavior for all foreign keys.


v0.3.4 - July 23, 2016 - YubiKey fix
------------------------------------

- Fix for YubiKey token encoding on Python 3.


v0.3.3 - January 10, 2016 - Python 3 cleanup
--------------------------------------------

- All modules include all four Python 3 __future__ imports for consistency.

- Migrations no longer have byte strings in them.


v0.3.2 - October 11, 2015 - Admin
---------------------------------

- Use ModelAdmin.raw_id_fields for foreign keys to users.


v0.3.0 - February 7, 2015 - Support Django migrations
-----------------------------------------------------

- otp_yubikey now has both Django and South migrations. Please see the `upgrade
  notes`_ for details on upgrading from previous versions.

.. _upgrade notes: https://pythonhosted.org/django-otp/overview.html#upgrading


v0.2.0 - November 10, 2013 - Django 1.6
---------------------------------------

- Now supports Django 1.4 to 1.6 on Python 2.6, 2.7, 3.2, and 3.3. This is the
  first release for Python 3.


v0.1.3 - October 2, 2013 - Unit test fixes
------------------------------------------

- The move away from fixtures inadvertantly made the tests sensitive to the
  primary keys allocated by the database.


v0.1.2 - May 9, 2013 - Unit test improvements
---------------------------------------------

- Major unit test cleanup. Tests should pass or be skipped under all supported
  versions of Django, with or without custom users and timzeone support.


v0.1.1 - May 8, 2013 - Packaging and test cleanup
-------------------------------------------------

- Include fixtures in the installation so the tests pass.


v0.1.0 - August 21, 2012 - Initial Release
------------------------------------------

Initial release.


.. vim: ft=rst nospell tw=80

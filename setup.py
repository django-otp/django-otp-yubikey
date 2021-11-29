#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name='django-otp-yubikey',
    version='1.0.1',
    description='A django-otp plugin that verifies YubiKey OTP tokens.',
    author='Peter Sagerson',
    author_email='psagers@ignorare.net',
    url='https://github.com/django-otp/django-otp-yubikey',
    project_urls={
        "Documentation": 'https://django-otp-yubikey.readthedocs.io/',
        "Source": 'https://github.com/django-otp/django-otp-yubikey',
    },
    license='BSD',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'django-otp >= 1.0.0',
        'YubiOTP >= 0.2.2',
    ],
)

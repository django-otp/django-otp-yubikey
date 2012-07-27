#!/bin/sh

make html

{ watchmedo-2.7 shell-command \
    -p '*.rst;*.py' \
    -R \
    -c echo \
    source ../otp_yubikey
} | while read line; do make html; done

import django.conf


class Settings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default values
    if they are not specified by the configuration.
    """
    defaults = {
        'OTP_YUBIKEY_API_ID': 1,
        'OTP_YUBIKEY_API_KEY': None,
        'OTP_YUBIKEY_DEFAULT_BASE_URL': '',
        'OTP_YUBIKEY_PROTOCOL_VERSION': '2.0',
        'OTP_YUBIKEY_SL': None,
        'OTP_YUBIKEY_TIMEOUT': None,
        'OTP_YUBIKEY_USE_SSL': False,
    }

    def __init__(self):
        """
        Loads our settings from django.conf.settings, applying defaults for any
        that are omitted.
        """
        for name, default in self.defaults.iteritems():
            value = getattr(django.conf.settings, name, default)
            setattr(self, name, value)


settings = Settings()

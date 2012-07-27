from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import YubikeyDevice, ValidationService, RemoteYubikeyDevice


class YubikeyDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_yubikey.models.YubikeyDevice`.
    """
    fieldsets = [
        ('Identity', {
            'fields': ['user', 'name', 'confirmed'],
        }),
        ('Configuration', {
            'fields': ['private_id', 'key'],
        }),
        ('State', {
            'fields': ['session', 'counter'],
        }),
    ]

    list_display = ['user', 'name', 'public_id']


class ValidationServiceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_yubikey.models.ValidationService`.
    """
    fieldsets = [
        ('Common Options', {
            'fields': ['name', 'api_id', 'api_key'],
        }),
        ('Other Options', {
            'fields': ['base_url', 'api_version', 'use_ssl', 'param_sl',
                       'param_timeout'],
        }),
    ]

    radio_fields = {'api_version': admin.HORIZONTAL}


class RemoteYubikeyDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_yubikey.models.RemoteYubikeyDevice`.
    """
    fieldsets = [
        ('Identity', {
            'fields': ['user', 'name', 'confirmed'],
        }),
        ('Configuration', {
            'fields': ['service', 'public_id'],
        }),
    ]


try:
    admin.site.register(YubikeyDevice, YubikeyDeviceAdmin)
    admin.site.register(ValidationService, ValidationServiceAdmin)
    admin.site.register(RemoteYubikeyDevice, RemoteYubikeyDeviceAdmin)
except AlreadyRegistered:
    # Useless exception triggered by multiple imports.
    pass

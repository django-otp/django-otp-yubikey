from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import YubikeyDevice, RemoteYubikeyDevice


class YubikeyDeviceAdmin(admin.ModelAdmin):
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


class RemoteYubikeyDeviceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identity', {
            'fields': ['user', 'name', 'confirmed'],
        }),
        ('Configuration', {
            'fields': ['public_id'],
        }),
        ('Validation', {
            'fields': ['api_version', 'api_id', 'api_key', 'use_ssl',
                       'param_sl', 'param_timeout', 'base_url'],
        }),
    ]

    radio_fields = {'api_version': admin.HORIZONTAL}


try:
    admin.site.register(YubikeyDevice, YubikeyDeviceAdmin)
    admin.site.register(RemoteYubikeyDevice, RemoteYubikeyDeviceAdmin)
except AlreadyRegistered:
    # Useless exception triggered by multiple imports.
    pass

from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import YubikeyDevice, RemoteYubikeyDevice


class YubikeyDeviceAdmin(admin.ModelAdmin):
    model = YubikeyDevice
    list_display = ['user', 'name', 'public_id']


class RemoteYubikeyDeviceAdmin(admin.ModelAdmin):
    model = RemoteYubikeyDevice


try:
    admin.site.register(YubikeyDevice, YubikeyDeviceAdmin)
    admin.site.register(RemoteYubikeyDevice, RemoteYubikeyDeviceAdmin)
except AlreadyRegistered:
    # Useless exception triggered by multiple imports.
    pass

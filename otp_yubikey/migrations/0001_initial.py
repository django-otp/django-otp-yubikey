# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import otp_yubikey.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteYubikeyDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text=b'Is this device ready for use?')),
                ('public_id', models.CharField(help_text=b'The public identity of the YubiKey (modhex-encoded).', max_length=32, verbose_name=b'Public ID')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Remote YubiKey device',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ValidationService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The name of this validation service.', max_length=32)),
                ('api_id', models.IntegerField(default=1, help_text=b'Your API ID.', verbose_name=b'API ID')),
                ('api_key', models.CharField(default=b'', help_text=b'Your base64-encoded API key.', max_length=64, verbose_name=b'API key', blank=True)),
                ('base_url', models.URLField(default=b'', help_text=b"The base URL of the verification service. Defaults to Yubico's hosted API.", verbose_name=b'Base URL', blank=True)),
                ('api_version', models.CharField(default=b'2.0', help_text=b'The version of the validation api to use.', max_length=8, choices=[(b'1.0', b'1.0'), (b'1.1', b'1.1'), (b'2.0', b'2.0')])),
                ('use_ssl', models.BooleanField(default=False, help_text=b'Use HTTPS API URLs by default?', verbose_name=b'Use SSL')),
                ('param_sl', models.CharField(default=None, help_text=b'The level of syncing required.', max_length=16, verbose_name=b'SL', blank=True)),
                ('param_timeout', models.CharField(default=None, help_text=b'The time to allow for syncing.', max_length=16, verbose_name=b'Timeout', blank=True)),
            ],
            options={
                'verbose_name': 'YubiKey validation service',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YubikeyDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text=b'Is this device ready for use?')),
                ('private_id', models.CharField(default=otp_yubikey.models.default_id, help_text=b'The 6-byte private ID (hex-encoded).', max_length=12, verbose_name=b'Private ID', validators=[otp_yubikey.models.id_validator])),
                ('key', models.CharField(default=otp_yubikey.models.default_key, help_text=b'The 16-byte AES key shared with this YubiKey (hex-encoded).', max_length=32, validators=[otp_yubikey.models.key_validator])),
                ('session', models.PositiveIntegerField(default=0, help_text=b'The non-volatile session counter most recently used by this device.')),
                ('counter', models.PositiveIntegerField(default=0, help_text=b'The volatile session usage counter most recently used by this device.')),
                ('user', models.ForeignKey(help_text=b'The user that this device belongs to.', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Local YubiKey device',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='remoteyubikeydevice',
            name='service',
            field=models.ForeignKey(to='otp_yubikey.ValidationService'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='remoteyubikeydevice',
            name='user',
            field=models.ForeignKey(help_text=b'The user that this device belongs to.', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]

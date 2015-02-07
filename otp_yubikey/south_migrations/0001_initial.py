# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'YubikeyDevice'
        db.create_table('otp_yubikey_yubikeydevice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('private_id', self.gf('django.db.models.fields.CharField')(default='8e95865dd658', max_length=12)),
            ('key', self.gf('django.db.models.fields.CharField')(default='6bbc4cb80665451ce089b3ef740f3ba2', max_length=32)),
            ('session', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('counter', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('otp_yubikey', ['YubikeyDevice'])

        # Adding model 'ValidationService'
        db.create_table('otp_yubikey_validationservice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('api_id', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('api_key', self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True)),
            ('base_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('api_version', self.gf('django.db.models.fields.CharField')(default='2.0', max_length=8)),
            ('use_ssl', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('param_sl', self.gf('django.db.models.fields.CharField')(default=None, max_length=16, blank=True)),
            ('param_timeout', self.gf('django.db.models.fields.CharField')(default=None, max_length=16, blank=True)),
        ))
        db.send_create_signal('otp_yubikey', ['ValidationService'])

        # Adding model 'RemoteYubikeyDevice'
        db.create_table('otp_yubikey_remoteyubikeydevice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('confirmed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['otp_yubikey.ValidationService'])),
            ('public_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('otp_yubikey', ['RemoteYubikeyDevice'])


    def backwards(self, orm):
        # Deleting model 'YubikeyDevice'
        db.delete_table('otp_yubikey_yubikeydevice')

        # Deleting model 'ValidationService'
        db.delete_table('otp_yubikey_validationservice')

        # Deleting model 'RemoteYubikeyDevice'
        db.delete_table('otp_yubikey_remoteyubikeydevice')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'otp_yubikey.remoteyubikeydevice': {
            'Meta': {'object_name': 'RemoteYubikeyDevice'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'public_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['otp_yubikey.ValidationService']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'otp_yubikey.validationservice': {
            'Meta': {'object_name': 'ValidationService'},
            'api_id': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'api_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'api_version': ('django.db.models.fields.CharField', [], {'default': "'2.0'", 'max_length': '8'}),
            'base_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'param_sl': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'blank': 'True'}),
            'param_timeout': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '16', 'blank': 'True'}),
            'use_ssl': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'otp_yubikey.yubikeydevice': {
            'Meta': {'object_name': 'YubikeyDevice'},
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'counter': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'8a54130234801a700476fbe32f67dc38'", 'max_length': '32'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'private_id': ('django.db.models.fields.CharField', [], {'default': "'a56b7fc16556'", 'max_length': '12'}),
            'session': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['otp_yubikey']
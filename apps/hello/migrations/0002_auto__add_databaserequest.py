# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DatabaseRequest'
        db.create_table(u'hello_databaserequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Request in database', max_length=30)),
            ('emergence', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=42, blank=True)),
        ))
        db.send_create_signal(u'hello', ['DatabaseRequest'])


    def backwards(self, orm):
        # Deleting model 'DatabaseRequest'
        db.delete_table(u'hello_databaserequest')


    models = {
        u'hello.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'hello.databaserequest': {
            'Meta': {'object_name': 'DatabaseRequest'},
            'emergence': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Request in database'", 'max_length': '30'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '42', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']
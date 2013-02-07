# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Composer'
        db.create_table('titles_composer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['Composer'])

        # Adding model 'Conductor'
        db.create_table('titles_conductor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['Conductor'])

        # Adding model 'Soloist'
        db.create_table('titles_soloist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['Soloist'])

        # Adding model 'Arranger'
        db.create_table('titles_arranger', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['Arranger'])

        # Adding model 'ConcertMaster'
        db.create_table('titles_concertmaster', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['ConcertMaster'])

        # Adding model 'Publisher'
        db.create_table('titles_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('titles', ['Publisher'])

        # Adding model 'OrchestraType'
        db.create_table('titles_orchestratype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('titles', ['OrchestraType'])

        # Adding model 'ScoreType'
        db.create_table('titles_scoretype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('titles', ['ScoreType'])

        # Adding model 'ConcertType'
        db.create_table('titles_concerttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('titles', ['ConcertType'])

        # Adding model 'SoloInstrument'
        db.create_table('titles_soloinstrument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('titles', ['SoloInstrument'])

        # Adding model 'Location'
        db.create_table('titles_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('titles', ['Location'])

        # Adding model 'Title'
        db.create_table('titles_title', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('composer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Composer'])),
            ('arranger', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Arranger'], null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Publisher'])),
            ('instrumentation', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('score_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.ScoreType'], null=True, blank=True)),
            ('orchestra_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.OrchestraType'], null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['Title'])

        # Adding M2M table for field solo_instruments on 'Title'
        db.create_table('titles_title_solo_instruments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('title', models.ForeignKey(orm['titles.title'], null=False)),
            ('soloinstrument', models.ForeignKey(orm['titles.soloinstrument'], null=False))
        ))
        db.create_unique('titles_title_solo_instruments', ['title_id', 'soloinstrument_id'])

        # Adding model 'Performance'
        db.create_table('titles_performance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Title'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('conductor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Conductor'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Location'])),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('concert_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.ConcertType'])),
            ('concert_master', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.ConcertMaster'])),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('titles', ['Performance'])

        # Adding M2M table for field soloist on 'Performance'
        db.create_table('titles_performance_soloist', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('performance', models.ForeignKey(orm['titles.performance'], null=False)),
            ('soloist', models.ForeignKey(orm['titles.soloist'], null=False))
        ))
        db.create_unique('titles_performance_soloist', ['performance_id', 'soloist_id'])

        # Adding model 'TitleNote'
        db.create_table('titles_titlenote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Title'])),
        ))
        db.send_create_signal('titles', ['TitleNote'])

        # Adding model 'PerformanceNote'
        db.create_table('titles_performancenote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('note', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('performance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['titles.Performance'])),
        ))
        db.send_create_signal('titles', ['PerformanceNote'])


    def backwards(self, orm):
        # Deleting model 'Composer'
        db.delete_table('titles_composer')

        # Deleting model 'Conductor'
        db.delete_table('titles_conductor')

        # Deleting model 'Soloist'
        db.delete_table('titles_soloist')

        # Deleting model 'Arranger'
        db.delete_table('titles_arranger')

        # Deleting model 'ConcertMaster'
        db.delete_table('titles_concertmaster')

        # Deleting model 'Publisher'
        db.delete_table('titles_publisher')

        # Deleting model 'OrchestraType'
        db.delete_table('titles_orchestratype')

        # Deleting model 'ScoreType'
        db.delete_table('titles_scoretype')

        # Deleting model 'ConcertType'
        db.delete_table('titles_concerttype')

        # Deleting model 'SoloInstrument'
        db.delete_table('titles_soloinstrument')

        # Deleting model 'Location'
        db.delete_table('titles_location')

        # Deleting model 'Title'
        db.delete_table('titles_title')

        # Removing M2M table for field solo_instruments on 'Title'
        db.delete_table('titles_title_solo_instruments')

        # Deleting model 'Performance'
        db.delete_table('titles_performance')

        # Removing M2M table for field soloist on 'Performance'
        db.delete_table('titles_performance_soloist')

        # Deleting model 'TitleNote'
        db.delete_table('titles_titlenote')

        # Deleting model 'PerformanceNote'
        db.delete_table('titles_performancenote')


    models = {
        'titles.arranger': {
            'Meta': {'ordering': "['last_name', 'first_name', 'middle_name', 'suffix']", 'object_name': 'Arranger'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'titles.composer': {
            'Meta': {'ordering': "['last_name', 'first_name', 'middle_name', 'suffix']", 'object_name': 'Composer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'titles.concertmaster': {
            'Meta': {'ordering': "['last_name', 'first_name', 'middle_name', 'suffix']", 'object_name': 'ConcertMaster'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'titles.concerttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ConcertType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'titles.conductor': {
            'Meta': {'ordering': "['last_name', 'first_name', 'middle_name', 'suffix']", 'object_name': 'Conductor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'titles.location': {
            'Meta': {'ordering': "['name']", 'object_name': 'Location'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'titles.orchestratype': {
            'Meta': {'ordering': "['name']", 'object_name': 'OrchestraType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'titles.performance': {
            'Meta': {'object_name': 'Performance'},
            'concert_master': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.ConcertMaster']"}),
            'concert_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.ConcertType']"}),
            'conductor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Conductor']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Location']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'soloist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['titles.Soloist']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Title']"})
        },
        'titles.performancenote': {
            'Meta': {'object_name': 'PerformanceNote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'performance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Performance']"})
        },
        'titles.publisher': {
            'Meta': {'ordering': "['name']", 'object_name': 'Publisher'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'titles.scoretype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ScoreType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'titles.soloinstrument': {
            'Meta': {'ordering': "['name']", 'object_name': 'SoloInstrument'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'titles.soloist': {
            'Meta': {'ordering': "['last_name', 'first_name', 'middle_name', 'suffix']", 'object_name': 'Soloist'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'titles.title': {
            'Meta': {'ordering': "['number']", 'object_name': 'Title'},
            'arranger': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Arranger']", 'null': 'True', 'blank': 'True'}),
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Composer']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instrumentation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'orchestra_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.OrchestraType']", 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Publisher']"}),
            'score_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.ScoreType']", 'null': 'True', 'blank': 'True'}),
            'solo_instruments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['titles.SoloInstrument']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'titles.titlenote': {
            'Meta': {'object_name': 'TitleNote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['titles.Title']"})
        }
    }

    complete_apps = ['titles']
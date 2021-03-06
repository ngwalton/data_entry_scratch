# Generated by Django 2.2.11 on 2020-03-13 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alpha',
            fields=[
                ('spec_id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False)),
                ('spec', models.CharField(help_text='Four letter alpha code', max_length=4, unique=True)),
                ('common', models.CharField(help_text='Common name', max_length=200, unique=True)),
                ('sci', models.CharField(help_text='Scientific name', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('entry_id', models.AutoField(db_index=True, editable=False, primary_key=True, serialize=False)),
                ('observer', models.CharField(help_text='Name of observer', max_length=200)),
                ('sid', models.CharField(help_text='Site id', max_length=10)),
                ('day', models.DateTimeField(help_text='Date of count')),
                ('entry', models.PositiveSmallIntegerField(help_text='First or second entry')),
                ('sky', models.PositiveSmallIntegerField(help_text='Sky condition')),
                ('tempc', models.PositiveSmallIntegerField(help_text='Temperature degrees C')),
            ],
        ),
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('obs_id', models.AutoField(db_index=True, editable=False, help_text='Observation id', primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('S', 'singing'), ('C', 'calling'), ('O', 'observed'), ('F', 'flyover')], help_text='Type of detection', max_length=1)),
                ('minute', models.PositiveSmallIntegerField(help_text='Minute of first detection')),
                ('entry_id', models.ForeignKey(help_text='Foreign key on Site entry_id', on_delete=django.db.models.deletion.CASCADE, to='bird_proj.Site')),
                ('spec_id', models.ForeignKey(help_text='Foreign key on Alpha spec (alpha code)', on_delete=django.db.models.deletion.PROTECT, to='bird_proj.Alpha')),
            ],
        ),
    ]

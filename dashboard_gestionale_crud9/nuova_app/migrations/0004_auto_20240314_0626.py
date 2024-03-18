# Generated by Django 3.2.23 on 2024-03-14 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuova_app', '0003_articoli'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articoli',
            name='codice_interno',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='deposito_scorte',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_deposito_scorte',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_estesa',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_famiglia',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_grstat_1',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_grstat_2',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_grstat_3',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_grstat_4',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_marca',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='descrizione_sottofamiglia',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='famiglia',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='gruppo_statistico_1',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='gruppo_statistico_2',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='gruppo_statistico_3',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='gruppo_statistico_4',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='indice_scorte_fabbisogno',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='livello_riordino',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='scorta_massima',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='scorta_minima',
        ),
        migrations.RemoveField(
            model_name='articoli',
            name='sottofamiglia',
        ),
    ]
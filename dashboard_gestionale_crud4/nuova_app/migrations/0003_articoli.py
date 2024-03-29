# Generated by Django 3.2.23 on 2024-03-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuova_app', '0002_auto_20240309_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articoli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ditta', models.DecimalField(decimal_places=0, default=1, max_digits=5)),
                ('codice', models.CharField(blank=True, max_length=25, null=True)),
                ('descrizione', models.CharField(blank=True, max_length=72, null=True)),
                ('descrizione_estesa', models.CharField(blank=True, max_length=1672, null=True)),
                ('codice_interno', models.CharField(blank=True, max_length=1672, null=True)),
                ('famiglia', models.CharField(blank=True, max_length=4, null=True)),
                ('descrizione_famiglia', models.CharField(blank=True, max_length=30, null=True)),
                ('sottofamiglia', models.CharField(blank=True, max_length=4, null=True)),
                ('descrizione_sottofamiglia', models.CharField(blank=True, max_length=30, null=True)),
                ('marca', models.CharField(blank=True, max_length=12, null=True)),
                ('descrizione_marca', models.CharField(blank=True, max_length=30, null=True)),
                ('gruppo_statistico_1', models.CharField(blank=True, max_length=30, null=True)),
                ('descrizione_grstat_1', models.CharField(blank=True, max_length=30, null=True)),
                ('gruppo_statistico_2', models.CharField(blank=True, max_length=30, null=True)),
                ('descrizione_grstat_2', models.CharField(blank=True, max_length=30, null=True)),
                ('gruppo_statistico_3', models.CharField(blank=True, max_length=30, null=True)),
                ('descrizione_grstat_3', models.CharField(blank=True, max_length=30, null=True)),
                ('gruppo_statistico_4', models.CharField(blank=True, max_length=30, null=True)),
                ('descrizione_grstat_4', models.CharField(blank=True, max_length=30, null=True)),
                ('deposito_scorte', models.CharField(blank=True, max_length=2, null=True)),
                ('descrizione_deposito_scorte', models.CharField(blank=True, max_length=40, null=True)),
                ('indice_scorte_fabbisogno', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
                ('scorta_minima', models.IntegerField(blank=True, null=True)),
                ('scorta_massima', models.IntegerField(blank=True, null=True)),
                ('livello_riordino', models.DecimalField(decimal_places=3, default=0, max_digits=14)),
            ],
            options={
                'verbose_name': 'Articolo',
                'verbose_name_plural': 'Articoli',
            },
        ),
    ]

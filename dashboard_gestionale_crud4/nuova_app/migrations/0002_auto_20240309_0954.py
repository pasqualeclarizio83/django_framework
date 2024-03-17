# Generated by Django 3.2.23 on 2024-03-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuova_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_deposito', models.CharField(blank=True, max_length=2, null=True)),
                ('descrizione', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Deposito',
                'verbose_name_plural': 'Depositi',
            },
        ),
        migrations.DeleteModel(
            name='Anagrafica',
        ),
    ]
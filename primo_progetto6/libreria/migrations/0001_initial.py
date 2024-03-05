# Generated by Django 3.2.23 on 2024-03-05 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.CharField(max_length=20)),
                ('nazione', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('isdn', models.CharField(max_length=13)),
                ('autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libri', to='libreria.autore')),
                ('genere', models.ManyToManyField(to='libreria.Genere')),
            ],
        ),
    ]

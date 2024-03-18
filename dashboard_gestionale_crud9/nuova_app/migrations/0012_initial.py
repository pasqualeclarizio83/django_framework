# Generated by Django 3.2.23 on 2024-03-18 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nuova_app', '0011_auto_20240318_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dipartimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Facolta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dipartimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.dipartimento')),
            ],
        ),
        migrations.CreateModel(
            name='Insegnamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('corso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.corso')),
            ],
        ),
        migrations.CreateModel(
            name='Studente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.CharField(max_length=100)),
                ('corso_di_laurea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.corso')),
            ],
        ),
        migrations.CreateModel(
            name='Professore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.CharField(max_length=100)),
                ('facolta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.facolta')),
            ],
        ),
        migrations.CreateModel(
            name='Iscrizione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insegnamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.insegnamento')),
                ('studente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.studente')),
            ],
        ),
        migrations.AddField(
            model_name='insegnamento',
            name='professore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.professore'),
        ),
        migrations.AddField(
            model_name='corso',
            name='facolta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuova_app.facolta'),
        ),
    ]

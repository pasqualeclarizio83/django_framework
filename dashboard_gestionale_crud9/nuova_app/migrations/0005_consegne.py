# Generated by Django 3.2.23 on 2024-03-14 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nuova_app', '0004_auto_20240314_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consegne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cap', models.CharField(blank=True, max_length=5, null=True)),
                ('qta', models.IntegerField(blank=True, null=True)),
                ('data_consegne', models.DateField(blank=True, null=True)),
                ('articolo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consegne_articolo', to='nuova_app.articoli')),
                ('deposito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consegne_deposito', to='nuova_app.deposito')),
            ],
            options={
                'verbose_name': 'Consegna',
                'verbose_name_plural': 'Consegne',
            },
        ),
    ]

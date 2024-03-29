# Generated by Django 3.2.15 on 2023-08-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuova_app', '0003_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

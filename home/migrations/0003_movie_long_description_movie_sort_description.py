# Generated by Django 4.2.13 on 2024-11-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_movieposter'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='long_Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='sort_Description',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
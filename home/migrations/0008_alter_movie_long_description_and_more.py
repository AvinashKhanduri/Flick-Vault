# Generated by Django 4.2.13 on 2024-11-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_movie_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='long_Description',
            field=models.TextField(default='Movies have always been a captivating medium for storytelling, transporting audiences to fantastical worlds, unraveling gripping mysteries, and exploring the depths of human emotion. From the golden age of cinema to the modern era of CGI-laden blockbusters, the art of filmmaking has evolved tremendously, leaving an indelible mark on cultures worldwide.'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='sort_Description',
            field=models.TextField(default='Movies have always been a', max_length=30),
        ),
    ]

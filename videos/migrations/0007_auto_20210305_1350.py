# Generated by Django 2.0.7 on 2021-03-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_film_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='movie_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

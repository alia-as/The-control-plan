# Generated by Django 2.0.7 on 2021-02-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_name',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]

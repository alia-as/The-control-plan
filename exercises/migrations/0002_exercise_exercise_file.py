# Generated by Django 2.0.7 on 2021-02-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exercise_file',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
    ]
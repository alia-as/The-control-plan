# Generated by Django 2.0.7 on 2021-03-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]

# Generated by Django 2.0.7 on 2021-02-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_exercise_exercise_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]

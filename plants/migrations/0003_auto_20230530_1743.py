# Generated by Django 3.2.18 on 2023-05-30 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='birthflower',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='meaning',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='preferences',
        ),
    ]

# Generated by Django 3.2.18 on 2023-05-30 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0003_garden_ex_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='garden',
        ),
    ]

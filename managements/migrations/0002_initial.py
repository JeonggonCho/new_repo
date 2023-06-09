# Generated by Django 3.2.18 on 2023-06-08 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('managements', '0001_initial'),
        ('plants', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.plant'),
        ),
        migrations.AddField(
            model_name='management',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='calenderentry',
            name='management',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.management'),
        ),
        migrations.AddField(
            model_name='calenderentry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

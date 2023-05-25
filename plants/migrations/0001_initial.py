# Generated by Django 3.2.18 on 2023-05-23 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import plants.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('preferences', models.CharField(max_length=20)),
                ('allergy', models.CharField(max_length=20)),
                ('flowering', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('watering', models.CharField(max_length=20)),
                ('sunlight', models.CharField(max_length=20)),
                ('humidity', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=20)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=plants.models.plant_images_path)),
                ('like_users', models.ManyToManyField(related_name='like_plants', to=settings.AUTH_USER_MODEL)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
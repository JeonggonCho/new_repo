# Generated by Django 3.2.18 on 2023-05-25 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='title',
            field=models.ForeignKey(default='뉴비', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.user_title'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
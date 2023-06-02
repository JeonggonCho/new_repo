# Generated by Django 3.2.18 on 2023-06-02 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastAlarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('broadcast_on', models.DateTimeField()),
                ('sent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-broadcast_on'],
            },
        ),
    ]
# Generated by Django 3.0.5 on 2021-03-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='title',
            new_name='ticker',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='completed',
        ),
        migrations.AddField(
            model_name='trade',
            name='move',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='time',
            field=models.DateTimeField(default='2021-01-01 06:00:00.000000-08:00'),
        ),
    ]

# Generated by Django 3.1.3 on 2021-01-14 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reus', '0003_auto_20201127_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='main_event',
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]

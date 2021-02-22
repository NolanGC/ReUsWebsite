# Generated by Django 3.1.3 on 2021-02-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reus', '0007_auto_20210219_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='quad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('highlight', models.BooleanField(default=False)),
                ('related_link', models.URLField(max_length=255)),
                ('body', models.TextField()),
                ('images', models.ImageField(upload_to='images/')),
                ('datestr', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='quadNext',
        ),
        migrations.DeleteModel(
            name='quadPrevious',
        ),
    ]

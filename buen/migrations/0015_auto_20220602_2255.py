# Generated by Django 3.2.13 on 2022-06-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buen', '0014_auto_20220529_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='archive',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='archive',
            name='time_created',
            field=models.TimeField(auto_now=True),
        ),
    ]

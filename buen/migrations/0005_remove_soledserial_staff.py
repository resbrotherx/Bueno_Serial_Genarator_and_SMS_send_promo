# Generated by Django 3.2.13 on 2022-05-19 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buen', '0004_soledserial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soledserial',
            name='staff',
        ),
    ]

# Generated by Django 4.0 on 2022-04-25 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genarator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genarator', models.CharField(max_length=900)),
                ('date_created', models.DateField(auto_now=True)),
                ('time_created', models.TimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('serial_number', models.CharField(max_length=200)),
                ('winner', models.CharField(max_length=200)),
                ('stock', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of stock', 'Out of stock'), ('Running Out of stock', 'Running Out of stock')], default='In Stock', max_length=400)),
                ('date_created', models.DateField(auto_now=True)),
                ('time_created', models.TimeField(auto_now=True)),
                ('date_sold', models.DateField()),
                ('time_sold', models.TimeField()),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]

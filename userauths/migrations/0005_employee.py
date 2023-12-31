# Generated by Django 5.0 on 2023-12-31 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('userauths', '0004_remove_dashboard_user_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_user', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=True)),
                ('bio', models.CharField(blank=True, max_length=100)),
                ('fname', models.CharField(blank=True, max_length=30)),
                ('lname', models.CharField(blank=True, max_length=30)),
                ('mname', models.CharField(blank=True, max_length=30)),
                ('mobilenumber', models.CharField(blank=True, max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photos/')),
                ('designation', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-23 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_alter_nguoidung_ngaysinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoidung',
            name='ngaysinh',
            field=models.DateField(default=datetime.datetime(2023, 5, 24, 2, 54, 28, 107064)),
        ),
    ]

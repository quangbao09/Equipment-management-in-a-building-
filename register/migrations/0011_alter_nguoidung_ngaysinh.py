# Generated by Django 4.2 on 2024-05-03 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_alter_nguoidung_ngaysinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoidung',
            name='ngaysinh',
            field=models.DateField(default=datetime.datetime(2024, 5, 3, 20, 56, 23, 73224)),
        ),
    ]

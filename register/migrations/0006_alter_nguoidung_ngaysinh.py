# Generated by Django 4.1.7 on 2023-05-22 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_nguoidung_diachi_alter_nguoidung_hoten_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoidung',
            name='ngaysinh',
            field=models.DateField(default=datetime.datetime(2023, 5, 22, 20, 14, 43, 445784)),
        ),
    ]
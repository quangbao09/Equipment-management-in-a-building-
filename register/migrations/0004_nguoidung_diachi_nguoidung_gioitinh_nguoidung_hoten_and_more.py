# Generated by Django 4.1.7 on 2023-05-22 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_nguoidung_matkhau_nguoidung_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='nguoidung',
            name='diachi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='gioitinh',
            field=models.CharField(choices=[('gioitinh1', 'Nam'), ('gioitinh2', 'Nữ'), ('gioitinh3', 'Khác')], default='gioitinh3', max_length=255),
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='hoten',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='ngaycapnhat',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='ngaysinh',
            field=models.DateField(default=datetime.datetime(2023, 5, 22, 19, 53, 27, 300385)),
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

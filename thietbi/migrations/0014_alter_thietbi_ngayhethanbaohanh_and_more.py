# Generated by Django 4.2 on 2024-05-03 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thietbi', '0013_alter_thietbi_ngayhethanbaohanh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thietbi',
            name='ngayhethanbaohanh',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 20, 56, 23, 75954)),
        ),
        migrations.AlterField(
            model_name='thietbi',
            name='ngaykiemtradinhky',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 20, 56, 23, 75954)),
        ),
        migrations.AlterField(
            model_name='thietbi',
            name='ngaymua',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 3, 20, 56, 23, 75954)),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-07 13:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('garyve', '0009_auto_20181207_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 13, 17, 33, 813534, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.1 on 2018-10-23 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181023_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 23, 17, 40, 18, 327601, tzinfo=utc)),
        ),
    ]

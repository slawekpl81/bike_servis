# Generated by Django 3.0.4 on 2020-03-30 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_base', '0002_auto_20200330_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servis',
            name='end_date',
            field=models.DateField(default=datetime.date(2020, 4, 5)),
        ),
    ]

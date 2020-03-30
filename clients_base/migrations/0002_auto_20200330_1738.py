# Generated by Django 3.0.4 on 2020-03-30 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='servis',
            name='end_date',
            field=models.DateField(default=datetime.date(2020, 4, 4)),
        ),
    ]
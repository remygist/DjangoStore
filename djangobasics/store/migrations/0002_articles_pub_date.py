# Generated by Django 5.1.2 on 2024-10-15 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 13, 35, 49, 690827, tzinfo=datetime.timezone.utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
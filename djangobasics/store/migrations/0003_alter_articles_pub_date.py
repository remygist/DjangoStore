# Generated by Django 5.1.2 on 2024-10-15 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_articles_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 13, 36, 15, 906160, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
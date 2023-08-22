# Generated by Django 4.2.1 on 2023-07-10 20:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0033_notification_pemesanan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='pemesanan',
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 20, 48, 0, 871742, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkout',
            field=models.DateField(default=datetime.datetime(2023, 7, 10, 20, 48, 0, 871742, tzinfo=datetime.timezone.utc)),
        ),
    ]
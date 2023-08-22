# Generated by Django 4.2.1 on 2023-07-09 04:44

import beranda.models
import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0029_alter_pemesanan_id_pembayaran_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelanggan',
            name='tanggal_input',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='id_pembayaran',
            field=models.CharField(default=beranda.models.Pemesanan.generate_uuid, editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='id_pemesanan',
            field=models.CharField(default=beranda.models.Pemesanan.generate_uuid, editable=False, max_length=8),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 4, 44, 49, 70382, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkout',
            field=models.DateField(default=datetime.datetime(2023, 7, 9, 4, 44, 49, 70382, tzinfo=datetime.timezone.utc)),
        ),
    ]

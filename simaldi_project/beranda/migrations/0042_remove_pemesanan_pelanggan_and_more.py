# Generated by Django 4.2.1 on 2023-08-13 11:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0041_remove_nomor_kamar_status_kamar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pemesanan',
            name='pelanggan',
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='alamat_pelanggan',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='foto_ktp',
            field=models.ImageField(blank=True, null=True, upload_to='ktp_images'),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='jenis_kelamin_pelanggan',
            field=models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='nama_pelanggan',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='no_ktp_pelanggan',
            field=models.CharField(max_length=16, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Hanya angka yang diperbolehkan')]),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='no_telepon_pelanggan',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Hanya angka yang diperbolehkan')]),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.datetime(2023, 8, 13, 11, 46, 20, 514470, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkout',
            field=models.DateField(default=datetime.datetime(2023, 8, 13, 11, 46, 20, 514470, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Pelanggan',
        ),
    ]
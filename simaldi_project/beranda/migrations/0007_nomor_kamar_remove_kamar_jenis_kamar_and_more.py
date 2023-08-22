# Generated by Django 4.2.1 on 2023-06-18 07:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0006_pemesanan_status_konfirmasi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomor_Kamar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_kamar', models.CharField(choices=[('VVIP', 'VVIP'), ('Executive Class', 'Executive Class'), ('Superior Room', 'Superior Room'), ('Deluxe Room', 'Deluxe Room')], max_length=50)),
                ('no_kamar', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Hanya angka yang diperbolehkan')])),
                ('status_kamar', models.CharField(choices=[('Full Booked', 'Full Booked'), ('Booked', 'Booked'), ('Empty Room', 'Empty Room')], default='Empty Room', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='kamar',
            name='jenis_kamar',
        ),
        migrations.RemoveField(
            model_name='kamar',
            name='no_kamar',
        ),
        migrations.RemoveField(
            model_name='kamar',
            name='status_kamar',
        ),
        migrations.RemoveField(
            model_name='pemesanan',
            name='no_kamar',
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='no_ktp_pelanggan',
            field=models.CharField(default=12345, max_length=16, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Hanya angka yang diperbolehkan')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='status_konfirmasi',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='kamar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pemesanan', to='beranda.kamar'),
        ),
        migrations.AddField(
            model_name='pemesanan',
            name='waktu_konfirmasi',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='status_konfirmasi',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.date(2023, 6, 18)),
        ),
        migrations.AddField(
            model_name='kamar',
            name='nomor_kamar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kamar', to='beranda.nomor_kamar'),
        ),
    ]

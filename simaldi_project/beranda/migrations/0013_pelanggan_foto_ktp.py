# Generated by Django 4.2.1 on 2023-06-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0012_alter_pemesanan_tanggal_checkin_kunci'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelanggan',
            name='foto_ktp',
            field=models.ImageField(blank=True, null=True, upload_to='ktp_images'),
        ),
    ]

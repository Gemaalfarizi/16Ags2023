# Generated by Django 4.2.1 on 2023-06-18 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0008_rename_nomor_kamar_kamar_jenis_kamar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemesanan',
            name='no_kamar_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beranda.nomor_kamar'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0014_remove_pemesanan_pesanan_khusus'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemesanan',
            name='id_pemesanan',
            field=models.CharField(default='53510', editable=False, max_length=50),
        ),
    ]
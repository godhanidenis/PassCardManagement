# Generated by Django 3.1.7 on 2021-04-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_auto_20210403_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='residence',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=4303, max_length=120, unique=True),
        ),
    ]
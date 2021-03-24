# Generated by Django 3.1.7 on 2021-03-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20210322_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=1873, max_length=120, unique=True),
        ),
    ]

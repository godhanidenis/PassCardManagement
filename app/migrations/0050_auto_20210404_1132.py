# Generated by Django 3.1.7 on 2021-04-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20210404_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='passcode',
            field=models.CharField(blank=True, default=2339, max_length=120, unique=True),
        ),
    ]
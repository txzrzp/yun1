# Generated by Django 3.1.4 on 2021-01-05 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201217_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='是否是active'),
        ),
    ]
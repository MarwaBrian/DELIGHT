# Generated by Django 4.1.4 on 2023-02-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delight_Cakehouse", "0002_cookies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cakes",
            name="cake_type",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="cookies",
            name="cookie_flavor",
            field=models.CharField(max_length=100),
        ),
    ]

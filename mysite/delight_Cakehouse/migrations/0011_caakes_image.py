# Generated by Django 4.1.4 on 2023-02-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delight_Cakehouse", "0010_alter_caakes_in_stock"),
    ]

    operations = [
        migrations.AddField(
            model_name="caakes",
            name="Image",
            field=models.ImageField(default="default.jpg", upload_to="cake_images"),
        ),
    ]

# Generated by Django 4.2.6 on 2025-01-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UsersApp", "0002_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="cost",
            field=models.FloatField(default=0.0),
        ),
    ]

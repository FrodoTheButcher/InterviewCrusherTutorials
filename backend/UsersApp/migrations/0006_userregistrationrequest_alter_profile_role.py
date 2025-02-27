# Generated by Django 4.2.6 on 2025-01-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UsersApp", "0005_alter_profile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRegistrationRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("USER", "User"),
                            ("HOUSEKEEPER", "Housekeeper"),
                            ("MANAGER", "Manager"),
                            ("RECEPTIONIST", "Receptionist"),
                            ("DEVELOPER", "Developer"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="profile",
            name="role",
            field=models.CharField(
                choices=[
                    ("USER", "User"),
                    ("HOUSEKEEPER", "Housekeeper"),
                    ("MANAGER", "Manager"),
                    ("RECEPTIONIST", "Receptionist"),
                    ("DEVELOPER", "Developer"),
                ],
                default="USER",
                max_length=15,
            ),
        ),
    ]

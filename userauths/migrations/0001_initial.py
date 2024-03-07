# Generated by Django 4.2 on 2024-03-02 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dashboard_User",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("is_user", models.BooleanField(default=True)),
                ("is_employee", models.BooleanField(default=False)),
                ("bio", models.CharField(blank=True, max_length=100)),
                ("fname", models.CharField(blank=True, max_length=30)),
                ("lname", models.CharField(blank=True, max_length=30)),
                ("mname", models.CharField(blank=True, max_length=30)),
                ("mobilenumber", models.CharField(blank=True, max_length=15)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="user_photos/"),
                ),
                (
                    "collegename",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("graduation_year", models.PositiveIntegerField(blank=True, null=True)),
                ("education", models.CharField(blank=True, max_length=50, null=True)),
                ("github", models.CharField(blank=True, max_length=100, null=True)),
                ("linkedin", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "enrolled_batches",
                    models.ManyToManyField(
                        blank=True, related_name="enrolled_batch", to="course.batch"
                    ),
                ),
                (
                    "enrolled_courses",
                    models.ManyToManyField(
                        blank=True, related_name="enrolled_users", to="course.course"
                    ),
                ),
            ],
        ),
    ]
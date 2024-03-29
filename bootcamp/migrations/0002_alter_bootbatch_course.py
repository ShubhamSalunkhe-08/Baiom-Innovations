# Generated by Django 4.2 on 2024-03-21 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bootcamp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bootbatch",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="batches",
                to="bootcamp.bootcourse",
            ),
        ),
    ]
# Generated by Django 3.2.13 on 2022-06-15 10:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Add region bounding box fields
    """

    dependencies = [
        ("cms", "0031_unique_version_constraint"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="latitude_max",
            field=models.FloatField(
                blank=True,
                help_text="The top boundary of the region",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(-90.0),
                    django.core.validators.MaxValueValidator(90.0),
                ],
                verbose_name="maximum latitude",
            ),
        ),
        migrations.AddField(
            model_name="region",
            name="latitude_min",
            field=models.FloatField(
                blank=True,
                help_text="The bottom boundary of the region",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(-90.0),
                    django.core.validators.MaxValueValidator(90.0),
                ],
                verbose_name="minimum latitude",
            ),
        ),
        migrations.AddField(
            model_name="region",
            name="longitude_max",
            field=models.FloatField(
                blank=True,
                help_text="The right boundary of the region",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(-180.0),
                    django.core.validators.MaxValueValidator(180.0),
                ],
                verbose_name="maximum longitude",
            ),
        ),
        migrations.AddField(
            model_name="region",
            name="longitude_min",
            field=models.FloatField(
                blank=True,
                help_text="The left boundary of the region",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(-180.0),
                    django.core.validators.MaxValueValidator(180.0),
                ],
                verbose_name="minimum longitude",
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="postal_code",
            field=models.CharField(
                help_text="For districts, enter the postcode of the administrative headquarters.",
                max_length=10,
                verbose_name="postal code",
            ),
        ),
    ]

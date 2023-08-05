# Generated by Django 3.2.16 on 2022-11-07 12:53

from django.db import migrations, models

import integreat_cms.cms.models.pois.poi


class Migration(migrations.Migration):
    """
    Add opening hours for locations
    """

    dependencies = [
        ("cms", "0048_region_seo_enabled"),
    ]

    operations = [
        migrations.AddField(
            model_name="poi",
            name="opening_hours",
            field=models.JSONField(
                default=integreat_cms.cms.models.pois.poi.get_default_opening_hours,
                verbose_name="opening hours",
            ),
        ),
        migrations.AddField(
            model_name="poi",
            name="temporarily_closed",
            field=models.BooleanField(
                default=False,
                help_text="Whether or not the location is temporarily closed. The opening hours remain and are only hidden.",
                verbose_name="temporarily closed",
            ),
        ),
    ]

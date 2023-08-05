# Generated by Django 3.2.12 on 2022-04-03 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration file to rename the "location on map" field of the POI model
    """

    dependencies = [
        ("cms", "0020_alter_last_updated_field"),
    ]

    operations = [
        migrations.RenameField(
            model_name="poi",
            old_name="location_not_on_map",
            new_name="location_on_map",
        ),
        migrations.AlterField(
            model_name="poi",
            name="location_on_map",
            field=models.BooleanField(
                default=True,
                help_text="Tick if you want to show this location on map",
                verbose_name="Show this location on map",
            ),
        ),
    ]

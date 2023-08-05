# Generated by Django 3.2.18 on 2023-05-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Add education icon to selection for location categories
    """

    dependencies = [
        ("cms", "0069_feedback_archived"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poicategory",
            name="icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("culture", "Culture"),
                    ("education", "Education"),
                    ("gastronomy", "Gastronomy"),
                    ("health", "Health"),
                    ("house", "House"),
                    ("leisure", "Leisure"),
                    ("media", "Media"),
                    ("meeting_point", "Meeting point"),
                    ("mobility", "Mobility"),
                    ("office", "Office"),
                    ("other", "Other"),
                    ("service", "Service"),
                    ("shopping", "Shopping"),
                ],
                help_text="Select an icon for this category",
                max_length=256,
                null=True,
                verbose_name="icon",
            ),
        ),
    ]

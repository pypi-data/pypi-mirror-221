# Generated by Django 3.2.12 on 2022-04-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration file that adds a tunews_enabled key to the region model
    """

    dependencies = [
        ("cms", "0015_user_unique_email_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="tunews_enabled",
            field=models.BooleanField(
                default=False,
                help_text="Enable to show a feed of tunews articles to users.",
                verbose_name="Enable tunews",
            ),
        ),
    ]

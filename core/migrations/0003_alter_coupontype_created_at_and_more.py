# Generated by Django 5.2.4 on 2025-07-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_remove_coupontype_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coupontype",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="coupontype",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

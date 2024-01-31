# Generated by Django 5.0.1 on 2024-01-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pissmap", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="piss",
            name="latitude",
            field=models.DecimalField(decimal_places=6, max_digits=6),
        ),
        migrations.AlterField(
            model_name="piss",
            name="longitude",
            field=models.DecimalField(decimal_places=6, max_digits=6),
        ),
        migrations.AlterField(
            model_name="piss",
            name="text",
            field=models.BinaryField(max_length=200),
        ),
    ]

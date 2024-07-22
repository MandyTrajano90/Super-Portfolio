# Generated by Django 4.2.3 on 2024-07-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_alter_certificate_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="profiles",
            field=models.ManyToManyField(
                related_name="certificates", to="projects.profile"
            ),
        ),
    ]

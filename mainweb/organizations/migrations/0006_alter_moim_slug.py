# Generated by Django 4.1 on 2022-08-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0005_alter_moim_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moim",
            name="slug",
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]

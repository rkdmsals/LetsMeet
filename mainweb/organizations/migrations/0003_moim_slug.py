# Generated by Django 4.1 on 2022-08-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "organizations",
            "0002_moim_admin_user_moim_end_date_moim_start_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="moim",
            name="slug",
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]

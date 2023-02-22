# Generated by Django 4.1.3 on 2023-02-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_stori_published_date_alter_stori_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stori",
            name="status",
            field=models.CharField(
                choices=[("draft", "draft"), ("published", "published")],
                default="drafted",
                max_length=20,
            ),
        ),
    ]

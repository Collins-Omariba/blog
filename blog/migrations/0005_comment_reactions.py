# Generated by Django 4.1.3 on 2023-02-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_comment_post_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="reactions",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

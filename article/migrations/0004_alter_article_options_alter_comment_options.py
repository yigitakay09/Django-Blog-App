# Generated by Django 4.2.7 on 2023-11-25 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"ordering": ["-created_date"]},
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-comment_date"]},
        ),
    ]

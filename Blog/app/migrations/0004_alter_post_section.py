# Generated by Django 4.2.9 on 2024-02-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_post_main_post_alter_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="section",
            field=models.CharField(
                choices=[
                    ("Popular", "Popular"),
                    ("Recent", "Recent"),
                    ("Editors_Pick", "Editors_Pick"),
                    ("Trending", "Trending"),
                    ("Inspiration", "Inspiration"),
                    ("Latest_Posts", "Latest_Posts"),
                ],
                max_length=200,
            ),
        ),
    ]

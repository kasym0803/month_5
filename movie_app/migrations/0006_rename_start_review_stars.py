# Generated by Django 5.0 on 2023-12-23 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_review_start_alter_review_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='start',
            new_name='stars',
        ),
    ]
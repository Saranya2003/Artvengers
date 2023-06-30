# Generated by Django 4.0 on 2023-06-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0015_rename_name_comment_artist_name_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='Cover_Photo',
        ),
        migrations.RemoveField(
            model_name='album',
            name='Description',
        ),
        migrations.AddField(
            model_name='artworkpost',
            name='Sensitive_content',
            field=models.BooleanField(default=False),
        ),
    ]
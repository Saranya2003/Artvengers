# Generated by Django 4.0 on 2023-04-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0005_rename_albumartist_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='albumTitle',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='artworkpost',
            old_name='imageUploader',
            new_name='Artwork',
        ),
        migrations.RenameField(
            model_name='artworkpost',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='artworkpost',
            old_name='artTitle',
            new_name='Tag',
        ),
        migrations.AddField(
            model_name='album',
            name='CoverPhoto',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/'),
        ),
        migrations.AddField(
            model_name='album',
            name='Description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artworkpost',
            name='Title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

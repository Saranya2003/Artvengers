# Generated by Django 4.0 on 2023-05-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0011_rename_social_media_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('post_date', models.DateTimeField()),
                ('Cover_Photo', models.ImageField(blank=True, null=True, upload_to='media/img/album_cover')),
            ],
        ),
        migrations.CreateModel(
            name='ArtWorkDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('post_date', models.DateTimeField()),
                ('Artwork', models.ImageField(blank=True, null=True, upload_to='media/img/')),
            ],
        ),
    ]
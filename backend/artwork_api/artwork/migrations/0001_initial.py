# Generated by Django 4.0 on 2023-06-30 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtworkPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('Description', models.TextField()),
                ('Sensitive_content', models.BooleanField(default=False)),
                ('Artwork', models.FileField(blank=True, upload_to='media/img/')),
                ('Tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('artist_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('likes', models.ManyToManyField(related_name='artwork_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='media/img/profile_pic')),
                ('Instagram', models.CharField(max_length=255)),
                ('Twitter', models.CharField(max_length=255)),
                ('Facebook', models.CharField(max_length=255)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork_comment', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('artist_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='artwork.artworkpost')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_Title', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('Private_Album', models.BooleanField(default=False)),
                ('artist_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('memberpic', models.ManyToManyField(related_name='artwork_post', to='artwork.ArtworkPost')),
            ],
        ),
    ]

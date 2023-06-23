# Generated by Django 4.0 on 2023-06-23 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('artwork', '0021_artworkpost_album_alter_artworkpost_artwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='artist_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]

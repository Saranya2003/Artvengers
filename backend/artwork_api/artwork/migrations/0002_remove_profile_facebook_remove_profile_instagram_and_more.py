# Generated by Django 4.0 on 2023-06-30 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Facebook',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Instagram',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Twitter',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthUser', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
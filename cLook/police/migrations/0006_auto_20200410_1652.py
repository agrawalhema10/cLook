# Generated by Django 3.0.2 on 2020-04-10 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0005_criminaldetails_social_media_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminaldetails',
            name='photo',
            field=models.ImageField(upload_to='cLook/'),
        ),
    ]

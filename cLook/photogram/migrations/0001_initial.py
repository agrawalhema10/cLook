# Generated by Django 3.0.2 on 2020-04-07 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50, null=True)),
                ('password', models.CharField(default='', max_length=50, null=True)),
                ('email', models.CharField(default='', max_length=50, null=True)),
                ('location', models.CharField(default='', max_length=50, null=True)),
                ('profile_pic', models.ImageField(upload_to='gallery/')),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='place',
            new_name='city',
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20201023_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]

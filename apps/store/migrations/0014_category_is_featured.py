# Generated by Django 3.1 on 2020-10-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-31 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20180731_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlentry',
            old_name='full_url',
            new_name='url',
        ),
        migrations.AddField(
            model_name='urlentry',
            name='shortened_url',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]

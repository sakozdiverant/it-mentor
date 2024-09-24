# Generated by Django 5.1.1 on 2024-09-18 09:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_profile_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='inn',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
    ]

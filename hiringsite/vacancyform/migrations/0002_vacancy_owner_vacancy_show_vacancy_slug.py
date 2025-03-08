# Generated by Django 5.1.6 on 2025-03-08 11:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyform', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='show',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]

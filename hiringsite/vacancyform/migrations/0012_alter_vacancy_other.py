# Generated by Django 5.1.6 on 2025-03-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyform', '0011_delete_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='other',
            field=models.TextField(blank=True, max_length=100000, verbose_name='Описание'),
        ),
    ]

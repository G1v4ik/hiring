# Generated by Django 5.1.6 on 2025-03-09 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyform', '0006_remove_vacancy_slug_vacancy_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='img',
        ),
    ]

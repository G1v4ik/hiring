# Generated by Django 5.1.6 on 2025-03-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyform', '0007_remove_vacancy_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='company',
            field=models.CharField(max_length=300, null=True, verbose_name='Организация / Компания'),
        ),
    ]

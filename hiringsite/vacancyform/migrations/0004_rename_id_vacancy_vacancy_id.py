# Generated by Django 5.1.6 on 2025-03-08 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyform', '0003_alter_vacancy_id_alter_vacancy_other_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='id',
            new_name='vacancy_id',
        ),
    ]

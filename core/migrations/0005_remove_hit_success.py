# Generated by Django 4.1.4 on 2022-12-19 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_hitstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hit',
            name='success',
        ),
    ]

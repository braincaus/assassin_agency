# Generated by Django 4.1.4 on 2022-12-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_hitman_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='HitStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]
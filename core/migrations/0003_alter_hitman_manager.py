# Generated by Django 4.1.4 on 2022-12-17 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_hitman_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hitman',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.hitman'),
        ),
    ]

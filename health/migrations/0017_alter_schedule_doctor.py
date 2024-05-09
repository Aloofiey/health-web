# Generated by Django 5.0.3 on 2024-05-01 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0016_appointment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='health.doctor'),
        ),
    ]

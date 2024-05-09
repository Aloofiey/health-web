# Generated by Django 5.0.3 on 2024-04-04 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_delete_admin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientappointment',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='patientappointment',
            name='patient',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('doctor', 'date', 'time')},
            },
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='PatientAppointment',
        ),
    ]
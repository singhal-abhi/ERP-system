# Generated by Django 4.0.5 on 2023-01-14 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_mark_attendance_semester_mark_attendance_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark_attendance',
            name='session',
            field=models.IntegerField(default=2023, editable=False, validators=[django.core.validators.MaxValueValidator(2023)]),
        ),
    ]

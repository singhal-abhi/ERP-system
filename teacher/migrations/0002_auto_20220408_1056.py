# Generated by Django 3.2 on 2022-04-08 05:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='teacherlogin',
            managers=[
                ('teach_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='teacherlogin',
            name='isactive',
            field=models.IntegerField(null=True),
        ),
    ]

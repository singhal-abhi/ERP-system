# Generated by Django 4.0.5 on 2022-07-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('batch', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=25)),
                ('fac', models.CharField(max_length=25)),
                ('loc', models.CharField(max_length=25)),
            ],
        ),
    ]

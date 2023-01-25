# Generated by Django 4.0.5 on 2022-12-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0016_subjects_to2_subjects_to3_subjects_to4_subjects_to5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='to1',
            field=models.CharField(help_text='Enter topics seperated by ,', max_length=500, verbose_name='Topics in Unit 1'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='to2',
            field=models.CharField(help_text='Enter topics seperated by ,', max_length=500, verbose_name='Topics in Unit 2'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='to3',
            field=models.CharField(help_text='Enter topics seperated by ,', max_length=500, verbose_name='Topics in Unit 3'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='to4',
            field=models.CharField(help_text='Enter topics seperated by ,', max_length=500, verbose_name='Topics in Unit 4'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='to5',
            field=models.CharField(help_text='Enter topics seperated by ,', max_length=500, verbose_name='Topics in Unit 5'),
        ),
    ]

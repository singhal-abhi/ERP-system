# Generated by Django 4.0.5 on 2023-03-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0028_question_ques'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_paper',
            name='marks_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_10',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_8',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question_paper',
            name='marks_9',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

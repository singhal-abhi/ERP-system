# Generated by Django 4.0.5 on 2023-03-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0027_remove_question_paper_ques1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ques',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

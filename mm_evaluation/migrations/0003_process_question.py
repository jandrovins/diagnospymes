# Generated by Django 3.0.3 on 2020-03-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm_evaluation', '0002_answer_archive_autoevaluation_financesinformation_process_pyme_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='question',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]

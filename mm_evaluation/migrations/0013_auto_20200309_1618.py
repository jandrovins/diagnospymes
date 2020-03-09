# Generated by Django 3.0.3 on 2020-03-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm_evaluation', '0012_auto_20200309_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoevaluation',
            name='final_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_10_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_1_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_2_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_3_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_4_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_5_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_6_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_7_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_8_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='autoevaluation',
            name='macroprocess_9_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]

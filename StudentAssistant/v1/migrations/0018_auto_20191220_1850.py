# Generated by Django 2.1.4 on 2019-12-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0017_evaluationscripts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationscripts',
            name='option1_input',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evaluationscripts',
            name='option2_input',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evaluationscripts',
            name='option3_input',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evaluationscripts',
            name='option4_input',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evaluationscripts',
            name='option5_input',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='evaluationscripts',
            name='option6_input',
            field=models.CharField(max_length=100),
        ),
    ]
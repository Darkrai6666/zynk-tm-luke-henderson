# Generated by Django 5.2 on 2025-04-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTM', '0005_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

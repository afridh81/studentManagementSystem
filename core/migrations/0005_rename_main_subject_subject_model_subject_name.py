# Generated by Django 3.2.4 on 2021-06-15 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_dept_department_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject_model',
            old_name='main_subject',
            new_name='subject_name',
        ),
    ]
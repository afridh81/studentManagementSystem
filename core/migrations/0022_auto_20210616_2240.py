# Generated by Django 3.2.4 on 2021-06-16 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_answerkeypaper_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer_key_details',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer_key_details',
            name='answer_key',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.answerkeypaper'),
        ),
    ]
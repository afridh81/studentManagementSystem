# Generated by Django 3.2.4 on 2021-06-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_answer_details_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='count_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True)),
            ],
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-16 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_answer_details_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerKeyPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_sheet', models.FileField(null=True, upload_to='Files/answer_keyss')),
                ('count', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='answer_details',
            name='answer_words',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.CreateModel(
            name='Answer_key_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_pages', models.CharField(max_length=5, null=True)),
                ('answer_key_words', models.CharField(max_length=5000, null=True)),
                ('count', models.IntegerField(null=True)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.answerkeypaper')),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.exam')),
            ],
        ),
    ]

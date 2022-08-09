# Generated by Django 3.2.4 on 2021-06-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_semester_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.exam')),
                ('teacher_evaluated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='Files/answers')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exam', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.exam')),
            ],
        ),
    ]

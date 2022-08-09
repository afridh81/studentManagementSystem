# Generated by Django 3.2.4 on 2021-06-15 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_answerpaper_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answerpaper',
            name='created',
        ),
        migrations.RemoveField(
            model_name='answerpaper',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='answerpaper',
            name='file',
        ),
        migrations.AddField(
            model_name='answerpaper',
            name='answer_sheet',
            field=models.FileField(null=True, upload_to='Files/answers'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.answerpaper')),
                ('exam', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.exam')),
            ],
        ),
    ]

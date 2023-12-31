# Generated by Django 4.2.6 on 2023-10-26 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_remove_answer_answers_answer_submitted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='submitted',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='base.submittedanswer'),
        ),
        migrations.AddField(
            model_name='choice',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='choice',
            name='is_answer',
            field=models.BooleanField(default=False),
        ),
    ]

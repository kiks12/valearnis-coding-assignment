# Generated by Django 4.2.6 on 2023-10-26 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_answer_index'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuizResult',
        ),
    ]

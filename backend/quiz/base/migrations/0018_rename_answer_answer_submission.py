# Generated by Django 4.2.6 on 2023-10-26 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_submittedanswer_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='submission',
        ),
    ]

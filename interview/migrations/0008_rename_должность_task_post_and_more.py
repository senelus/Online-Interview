# Generated by Django 4.0.4 on 2022-05-26 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0007_rename_post_task_должность_remove_user_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Должность',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Должность',
            new_name='post',
        ),
    ]

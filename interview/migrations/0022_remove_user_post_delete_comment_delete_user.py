# Generated by Django 4.0.4 on 2022-05-26 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0021_user_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

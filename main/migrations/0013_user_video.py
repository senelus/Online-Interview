# Generated by Django 4.0.4 on 2022-06-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_user_date_of_passage_posix'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Видео с веб-камеры'),
        ),
    ]

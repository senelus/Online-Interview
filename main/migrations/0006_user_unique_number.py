# Generated by Django 4.0.4 on 2022-05-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_question_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='unique_number',
            field=models.CharField(default=1, max_length=15, verbose_name='Уникальный код'),
            preserve_default=False,
        ),
    ]
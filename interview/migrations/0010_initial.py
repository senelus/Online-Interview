# Generated by Django 4.0.4 on 2022-05-26 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interview', '0009_remove_task_post_remove_user_comments_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspector', models.CharField(max_length=50, verbose_name='Проверяющий')),
                ('comment', models.TextField(verbose_name='Комментарий проверяющего')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'должность',
                'verbose_name_plural': 'должности',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, verbose_name='Отчество')),
                ('date_of_passage', models.DateTimeField(verbose_name='Дата прохождения интервью')),
                ('comments', models.ManyToManyField(related_name='Комментарии', to='interview.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.post')),
            ],
            options={
                'verbose_name': 'участник',
                'verbose_name_plural': 'участники',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название задания')),
                ('text', models.TextField(verbose_name='Описание задания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.post')),
            ],
            options={
                'verbose_name': 'задание',
                'verbose_name_plural': 'задания',
            },
        ),
    ]

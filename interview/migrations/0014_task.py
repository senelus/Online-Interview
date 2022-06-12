# Generated by Django 4.0.4 on 2022-05-26 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0013_delete_task'),
    ]

    operations = [
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

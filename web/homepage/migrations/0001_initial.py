# Generated by Django 4.1.2 on 2022-10-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название песни')),
                ('author', models.CharField(max_length=100, verbose_name='Исполнитель')),
                ('duration', models.CharField(max_length=10, verbose_name='Длительность')),
                ('file', models.TextField(verbose_name='Путь к файлу (mp3)')),
                ('uid', models.IntegerField(verbose_name='ID песни')),
            ],
        ),
    ]

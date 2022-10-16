from django.db import models

class Track(models.Model):
    title = models.CharField('Название песни', max_length=100)
    author = models.CharField('Исполнитель', max_length=100)
    duration = models.CharField('Длительность', max_length=10)
    file = models.TextField('Путь к файлу (mp3)')

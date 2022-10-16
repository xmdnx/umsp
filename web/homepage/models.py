from unittest.util import _MAX_LENGTH
from django.db import models

class Track(models.Model):
    title = models.CharField('Название песни', max_length=100)
    author = models.CharField('Исполнитель', max_length=100)
    duration = models.CharField('Длительность', max_length=10)
    file = models.FieldFile('Файл (mp3)')

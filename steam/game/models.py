from django.db import models


class GameGenre(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")


class GamePublisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")


class Game(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название")
    genre = models.ForeignKey(GameGenre, on_delete=models.CASCADE, verbose_name="Жанр")
    publisher = models.ForeignKey(GamePublisher, on_delete=models.CASCADE, verbose_name="Издатель")
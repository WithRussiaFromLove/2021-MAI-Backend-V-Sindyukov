from django.db import models
from user.models import User
from game.models import Game


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Авто")
    price = models.IntegerField(verbose_name="Цена")
    date = models.DateField()
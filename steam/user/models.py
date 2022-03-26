from django.db import models

# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=32, verbose_name="Страна")
    city = models.CharField(max_length=32, verbose_name="Город")

class User(models.Model):
    nickname = models.CharField(max_length=32, verbose_name="Ник")
    first_name = models.CharField(max_length=32, verbose_name="Имя")
    last_name = models.CharField(max_length=32, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Почта")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Локация")
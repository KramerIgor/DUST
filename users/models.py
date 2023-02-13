from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    #Кастомная модель Юзера
    email = models.EmailField(unique=True)
    riot_id = models.CharField(max_length=100, blank=True, null=True)
    blizzard_id = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.username


class Currency(models.Model):
    #Модель валюты (например рубли)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='currency_icons/')

    def __str__(self):
        return self.name

class Wallet(models.Model):
    # Кошелек с количеством хранимых валют
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.user} - {self.currency}: {self.amount}"
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс создания экземпляра модели пользователя"""

    username = None

    email = models.EmailField(unique=True, verbose_name="Почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """Магический метод, возвращает email пользователя"""
        return self.email

    class Meta:
        """Метакласс модели пользователя"""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

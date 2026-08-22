from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс создания экземпляра модели пользователя"""

    username = None

    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name="Номер телефона")
    USERNAME_FIELD = "email"
    tg_chat_id = models.CharField(max_length=50, null=True, blank=True, verbose_name="Телеграмм chat_id")

    REQUIRED_FIELDS = []

    def __str__(self):
        """Магический метод, возвращает email пользователя"""
        return self.email

    class Meta:
        """Метакласс модели пользователя"""

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

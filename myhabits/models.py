from django.db import models

from users.models import User


class Habit(models.Model):
    """Класс создания экземпляра привычки"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель привычки", related_name="habits", )
    place = models.CharField(max_length=100, verbose_name="Место выполнения привычки", )
    date_time = models.DateTimeField(verbose_name="Время выполнения привычки", )
    habit = models.CharField(max_length=100, verbose_name="Полезная привычка", )
    is_pleasure = models.BooleanField(default=False, verbose_name="Признак приятной привычки", )
    connection_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="Связанная привычка", blank=True, null=True, related_name="habits", )
    period = models.PositiveIntegerField(default=1, verbose_name="Периодичность выполнения привычки", )
    present = models.CharField(max_length=100, verbose_name="Вознаграждение", blank=True, null=True, )
    time_habit = models.TimeField(verbose_name="Время на выполнение привычки", )
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности", )

    def __str__(self):
        """Магический метод, возвращает название привычки"""
        return self.habit

    class Meta:
        """Метакласс модели привычки"""

        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

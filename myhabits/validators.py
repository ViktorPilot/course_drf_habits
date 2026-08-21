from datetime import time
from rest_framework import serializers


def validate_connection_habit_or_present(connection_habit, present, is_pleasure):
    """Метод валидирует добавление вознаграждения или приятной привычки в зависимости от признака привычки"""
    if connection_habit and present:
         raise serializers.ValidationError("Приятная привычка и вознаграждение не могут быть заполнены одновременно")
    elif is_pleasure and present:
        raise serializers.ValidationError("Для вознаграждения признак приятной привычки должен быть False.")
    elif not is_pleasure and connection_habit:
        raise serializers.ValidationError("Для связанной привычки признак приятной привычки должен быть True.")
    elif connection_habit:
        if connection_habit.connection_habit or connection_habit.present or connection_habit.is_pleasure:
            raise serializers.ValidationError("Cвязанная привычка не должна иметь вознаграждения или другой связанной привычки")

def validate_time_habit(time_habit):
    """Метод валидирует время выполнения привычки не более 120 секунд"""
    max_time_habit = time(hour=0, minute=2, second=0)
    if time_habit > max_time_habit:
        raise serializers.ValidationError("Время выполнения привычки должно быть менее 120 секунд")

def validate_habit_a_week(period):
    """Метод валидирует периодичность выполнения привычки не реже 1 раза в неделю"""
    if period:
        if period < 1:
            raise serializers.ValidationError("Периодичность выполнения привычки должна быть не реже 1 раза в неделю")

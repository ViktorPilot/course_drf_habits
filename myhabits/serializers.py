from rest_framework import serializers

from myhabits.models import Habit
from myhabits.validators import validate_connection_habit_or_present, validate_habit_a_week, validate_time_habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор экземпляра модели привычки"""

    class Meta:
        """Метакласс сериализатора привычки"""

        model = Habit
        fields = "__all__"

    def validate(self, attrs):
        """Метод валидирует привычку в зависимости от заданных заданием условий"""
        connection_habit = attrs.get("connection_habit")
        present = attrs.get("present")
        is_pleasure = attrs.get("is_pleasure")
        validate_connection_habit_or_present(connection_habit, present, is_pleasure)
        time_habit = attrs.get("time_habit")
        validate_time_habit(time_habit)
        period = attrs.get("period")
        validate_habit_a_week(period)
        return attrs

from rest_framework import serializers

from myhabits.models import Habit
from myhabits.validators import validate_connection_habit_or_present


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        """Метод валидирует привязку связанной привычки или вознаграждения"""
        connection_habit = attrs.get('connection_habit')
        present = attrs.get('present')
        validate_connection_habit_or_present(connection_habit, present)
        return attrs

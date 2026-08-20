from rest_framework import serializers


def validate_connection_habit_or_present(connection_habit, present):
    if connection_habit and present:
        raise serializers.ValidationError("Одновременный выбор связанной привычки и вознаграждения невозможен")
    elif not connection_habit and not present:
        raise serializers.ValidationError("Должно быть заполнено одно поле")
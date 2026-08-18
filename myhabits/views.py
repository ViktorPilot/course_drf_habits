from django.shortcuts import render
from rest_framework import generics
from myhabits.models import Habit
from myhabits.serializers import HabitSerializer


class HabiListAPIView(generics.ListAPIView):
    """Контроллер API списка привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated, IsModerators | IsOwner]
    # pagination_class = MyPagination


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Контроллер API редактирования существующей привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated, IsModerators | IsOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер API данных привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated, IsModerators | IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    """Контроллер API создания новой привычки"""

    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, ~IsModerators]

    # def perform_create(self, serializer):
    #     """Метод добавляет авторизованного пользователя в поле владельца лекции"""
    #     lesson = serializer.save()
    #     lesson.owner = self.request.user
    #     lesson.save()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Контроллер API удаления существующей привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes = [IsAuthenticated, ~IsModerators & IsOwner]

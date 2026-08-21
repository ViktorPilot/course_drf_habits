from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from myhabits.models import Habit
from myhabits.pagination import MyPagination
from myhabits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListAPIView(generics.ListAPIView):
    """Контроллер API списка привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = MyPagination

    def get_queryset(self):
        """Метод фильтрует привычки по текущему пользователю"""
        return Habit.objects.filter(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер API редактирования существующей привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер API данных привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер API создания новой привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     """Метод добавляет авторизованного пользователя в поле владельца лекции"""
    #     lesson = serializer.save()
    #     lesson.owner = self.request.user
    #     lesson.save()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Контроллер API удаления существующей привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

class AllHabitListAPIView(generics.ListAPIView):
    """Контроллер API списка привычек всех пользователей с признаком публичности True"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination
    def get_queryset(self):
        """Метод фильтрует привычки по признаку публичности True"""
        return Habit.objects.filter(is_public=True)
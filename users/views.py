from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer



class UserUpdateAPIView(generics.UpdateAPIView):
    """Контроллер API редактирования существующего пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    """Контроллер API просмотра списка пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер API просмотра профиля пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер API создания нового пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Метод устанавливает статус пользователя активным и хэширует пароль перед сохранением"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Контроллер API удаления пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

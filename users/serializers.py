from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор экземпляра модели пользователя"""

    class Meta:
        """Метакласс сериализатора модели пользователя"""

        model = User
        fields = "__all__"

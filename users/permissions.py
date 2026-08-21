from rest_framework import  permissions

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Метод проверяет является ли пользователь владельцем привычки"""
        return obj.owner == request.user

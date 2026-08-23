from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserAPITestCase(APITestCase):
    """Класс теста CRUD пользователя"""

    def setUp(self):
        """Метод добавления исходных данных для тестирования"""
        self.user = User.objects.create(email="test@ya.ru", phone="89998887766", tg_chat_id="333333333")
        self.user_3 = User.objects.create(email="test_3@ya.ru", phone="89990001000", tg_chat_id="11111111")
        self.client.force_authenticate(
            user=self.user,
        )

    def test_user_retrieve(self):
        """Тестирование вывода данных по пользователю"""
        url = reverse("users:user-detail", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), self.user.email)

    def test_user_create(self):
        """Тестирование создания пользователя"""
        url = reverse("users:user-register")
        data = {"email":"test_2@ya.ru", "phone":"89991112233", "tg_chat_id":"222222222", "password":"12345"}
        response = self.client.post(url, data, format="json", )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 3)

    def test_user_update(self):
        """Тестирование изменения данных по пользователю"""
        url = reverse("users:user-update", args=(self.user.pk,))
        data = {"email":"test@ya.ru", "phone":"89997775533", "tg_chat_id":"222222222", "password":"12345"}
        response = self.client.patch(url, data, format="json", )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("phone"), "89997775533")

    def test_user_delete(self):
        """Тестирование удаления пользователя"""
        url = reverse("users:user-delete", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 1)

    def test_user_list(self):
        """Тестирование вывода данных по всем пользователям"""
        url = reverse("users:user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 2)

from datetime import time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from myhabits.models import Habit
from users.models import User


class HabitAPITestCase(APITestCase):
    """Класс теста CRUD привычки"""

    def setUp(self):
        """Метод добавления исходных данных для тестирования"""
        self.user = User.objects.create(email="test@ya.ru", phone="89998887766", tg_chat_id="333333333")
        self.habit = Habit.objects.create(
            owner=self.user,
            place="дома",
            date_time="2026-08-23T18:27:00",
            habit="чистить зубы",
            is_pleasure=False,
            connection_habit=None,
            present="съесть пирожное",
            time_habit="00:02:00",
            is_public=True,
        )
        self.habit_2 = Habit.objects.create(
            owner=self.user,
            place="в гостях",
            date_time="2026-08-24T18:27:00",
            habit="улыбаться",
            time_habit="00:02:00",
            is_public=False,
        )
        self.client.force_authenticate(
            user=self.user,
        )

    def test_habit_retrieve(self):
        """Тестирование вывода данных по привычке"""
        url = reverse("myhabits:habit-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("habit"), self.habit.habit)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        url = reverse("myhabits:habit-create")
        data = {
            "owner": self.user.pk,
            "place": "на работе",
            "date_time": "2026-08-24T18:27:00",
            "habit": "работать",
            "is_pleasure": True,
            "connection_habit": self.habit_2.pk,
            "present": None,
            "time_habit": "00:01:00",
            "is_public": False,
        }
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 3)

    def test_habit_update(self):
        """Тестирование изменения данных по привычке"""
        url = reverse("myhabits:habit-update", args=(self.habit.pk,))
        data = {
            "owner": self.user.pk,
            "place": "дома",
            "date_time": "2026-08-24T18:27:00",
            "habit": "чистить зубы",
            "is_pleasure": False,
            "connection_habit": None,
            "present": "съесть торт",
            "time_habit": "00:02:00",
            "is_public": True,
        }
        response = self.client.patch(
            url,
            data,
            format="json",
        )
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("present"), "съесть торт")

    def test_habit_delete(self):
        """Тестирование удаления привычки"""
        url = reverse("myhabits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_list(self):
        """Тестирование вывода данных по всем привычкам пользователя"""
        url = reverse("myhabits:habit-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "дома",
                    "date_time": "2026-08-23T18:27:00Z",
                    "habit": "чистить зубы",
                    "is_pleasure": False,
                    "period": 1,
                    "present": "съесть пирожное",
                    "time_habit": "00:02:00",
                    "is_public": True,
                    "owner": self.user.pk,
                    "connection_habit": None,
                },
                {
                    "id": self.habit_2.pk,
                    "place": "в гостях",
                    "date_time": "2026-08-24T18:27:00Z",
                    "habit": "улыбаться",
                    "is_pleasure": None,
                    "period": 1,
                    "present": None,
                    "time_habit": "00:02:00",
                    "is_public": False,
                    "owner": self.user.pk,
                    "connection_habit": None,
                },
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_list_all(self):
        """Тестирование вывода данных по всем привычкам со статусом публичной привычки True"""
        url = reverse("myhabits:habit-list-all")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": self.habit.pk,
                "place": "дома",
                "date_time": "2026-08-23T18:27:00Z",
                "habit": "чистить зубы",
                "is_pleasure": False,
                "period": 1,
                "present": "съесть пирожное",
                "time_habit": "00:02:00",
                "is_public": True,
                "owner": self.user.pk,
                "connection_habit": None,
            }
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_create_time_err(self):
        """Тестирование валидатора времени на выполнения привычки"""
        url = reverse("myhabits:habit-create")
        time_habit = time(minute=3)
        data = {
            "owner": self.user.pk,
            "place": "в космосе",
            "date_time": "2026-08-24T18:27:00",
            "habit": "спать",
            "is_pleasure": True,
            "connection_habit": self.habit_2.pk,
            "present": None,
            "time_habit": time_habit,
            "is_public": False,
        }
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(
            response.data["non_field_errors"][0],
            "Время выполнения привычки должно быть менее 120 секунд",
        )

    def test_habit_create_period_err(self):
        """Тестирование валидатора периодичности выполнения привычки"""
        url = reverse("myhabits:habit-create")
        time_habit = time(minute=1)
        data = {
            "owner": self.user.pk,
            "place": "в космосе",
            "date_time": "2026-08-24T18:27:00",
            "habit": "спать",
            "is_pleasure": True,
            "connection_habit": self.habit_2.pk,
            "present": None,
            "time_habit": time_habit,
            "is_public": False,
            "period": 0,
        }
        response = self.client.post(
            url,
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(
            response.data["non_field_errors"][0],
            "Периодичность выполнения привычки должна быть не реже 1 раза в неделю",
        )

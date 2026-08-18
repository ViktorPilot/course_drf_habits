from django.urls import path

from myhabits import apps
from myhabits.views import HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, HabitDestroyAPIView, \
    HabitRetrieveAPIView

app_name = apps.MyhabitsConfig.name

urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit-list"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habit/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habit/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit-delete"),
    path("habit/<int:pk>/retrieve/", HabitRetrieveAPIView.as_view(), name="habit-retrieve"),
]

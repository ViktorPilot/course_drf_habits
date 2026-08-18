from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myhabit/", include('myhabits.urls', namespace='habits')),
    path("user/", include("users.urls", namespace="users")),
]

"""Определяет URL щаблоны для пользователей"""

from django.urls import path, include


app_name = 'users'
urlpatterns = [
    # Включает аутентификацию URL по умолчанию
    path('', include('django.contrib.auth.urls')),
]

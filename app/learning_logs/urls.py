"""Определяет схемы URL для learning_logs"""
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница, которая показывает все статьи
    path('topics/', views.topics, name='topics'),
    # Отдельная страница для каждой статьи
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
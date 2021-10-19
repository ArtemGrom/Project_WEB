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
    # Страница для добавления новой статьи
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """Домашняя страница для приложения"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Показать все статьи"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Показывает единственную статью и все записи к ней"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topics.html', context)

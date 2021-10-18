from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm


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
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Добавляем новую статью"""
    if request.method != 'POST':
        # Данных нет, создаем пустую форму
        form = TopicForm()
    else:
        # Данные есть, обрабатываем данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Отображение пустой или недопустимой формы
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


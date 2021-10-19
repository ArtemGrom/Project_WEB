from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


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


def new_entry(request, topic_id):
    """Добавляем новую запись для определенной темы"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Данных нет, создаем пустую форму
        form = EntryForm()
    else:
        # POST данные предоставлены, обрабатываем
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Отображение пустой или недопустимой формы
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Редактирование существующей записи"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Начальный запрос, нужно заполнить форму сначала.
        form = EntryForm(instance=entry)
    else:
        # POST данные предоставлены, обрабатываем
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
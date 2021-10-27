from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Регистрация нового пользователя"""
    if request.method != 'POST':
        # Отображаем пустую регистрационную форму
        form = UserCreationForm()
    else:
        # Обрабатываем запрошенную форму
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Залогиниваем пользователя и затем перенаправляем на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')

    # Отображение пустой или невалидной формы
    context = {'form': form}
    return render(request, 'registration/register.html', context)

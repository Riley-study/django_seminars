from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from .models import Coin
from .forms import GameForm

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    return HttpResponse('Hello world!!')


# def heads_or_tails(request):
#     size = random.choice(["Орел", "Решка"])
#     coin = Coin(size=size)
#     coin.save()
#     return HttpResponse(f'{size}')


def coin_values(request):
    val = Coin.values()
    lst = []
    for i in val:
        lst.append(i.size)
    return HttpResponse(str(lst))


# def cube(request):
#     return HttpResponse(f'{random.randint(1, 6)}')
#
#
# def numbers(request):
#     return HttpResponse(f'{random.randint(1, 100)}')


# Homework 1

html_main = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello page</title>
</head>
<body>
<h1>Главная страница</h1>
<p>Это мой первый Django-сайт</p>
</body>
</html>
"""


def main_page(request):
    logger.info('successful opening the main page')
    return HttpResponse(html_main)


html_about_us = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>About us</title>
</head>
<body>
<h1>Страница обо мне</h1>
<p>Меня зовут Наталья</p>
<p>Я студентка Geek Brains</p>
<p>Специализация: Разработчик Python</p>
</body>
</html>
"""


def about_us(request):
    logger.info('successful opening page about us')
    return HttpResponse(html_about_us)


def heads_or_tails(request, count=5):
    lst = []
    for i in range(count):
        size = random.choice(["Орел", "Решка"])
        # coin = Coin(size=size)
        # coin.save()
        lst.append(size)
    context = {
        'game_name': 'Орел или решка',
        'value': lst,
        'count': count,
    }
    return render(request, 'gameapp/choose_game.html', context)


def cube(request, count=5):
    lst = []
    for i in range(count):
        res = random.randint(1, 6)
        lst.append(res)
    context = {
        'game_name': 'Бросаем кубик',
        'value': lst,
        'count': count,
    }
    return render(request, 'gameapp/choose_game.html', context)


def numbers(request, count=5):
    lst = []
    for i in range(count):
        res = random.randint(1, 100)
        lst.append(res)
    context = {
        'game_name': 'От 1 до 100',
        'value': lst,
        'count': count,
    }
    return render(request, 'gameapp/choose_game.html', context)


def game_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            attempts = form.cleaned_data['attempts']
            if game == 'coin':
                return heads_or_tails(request, count=attempts)
            if game == 'cube':
                return cube(request, count=attempts)
            if game == 'number':
                return numbers(request, count=attempts)
    else:
        form = GameForm()
    return render(request, 'gameapp/game_form.html', {'form': form})

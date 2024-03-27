from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from .models import Coin

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    return HttpResponse('Hello world!!')


def heads_or_tails(request):
    size = random.choice(["Орел", "Решка"])
    coin = Coin(size=size)
    coin.save()
    return HttpResponse(f'{size}')


def coin_values(request):
    val = Coin.values()
    lst = []
    for i in val:
        lst.append(i.size)
    return HttpResponse(str(lst))


def cube(request):
    return HttpResponse(f'{random.randint(1, 6)}')


def numbers(request):
    return HttpResponse(f'{random.randint(1, 100)}')


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

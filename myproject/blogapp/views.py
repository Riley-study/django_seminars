from django.http import HttpResponse
from django.shortcuts import render

from .models import Author


# Create your views here.

def view_authors(request):
    lst = []
    for i in range(5):
        author = Author(first_name=f'name{i}', second_name=f'second{i}', email=f'mail{i}@ex.ru',
                        biography=f'many_words{i}',
                        birthday=f'2000-11-06')
        author.save()
        lst.append(author.first_name)
    return HttpResponse(f'{lst}')


def index(request):
    context = {
        'name': 'Django project',
        'data': '29.03.2024'
    }
    return render(request, 'blogapp/index.html', context)


def about_us(request):
    context = {
        'name': 'Natalya',
        'study': 'GeekBrains',
        'subjects': ['Django', 'Flask', 'FastAPI']
    }
    return render(request, 'blogapp/about_us.html', context)
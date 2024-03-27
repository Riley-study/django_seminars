from django.http import HttpResponse
from .models import Author


# Create your views here.
def index(request):
    return HttpResponse('Hello world!!')


def view_authors(request):
    lst = []
    for i in range(5):
        author = Author(first_name=f'name{i}', second_name=f'second{i}', email=f'mail{i}@ex.ru',
                        biography=f'many_words{i}',
                        birthday=f'2000-11-06')
        author.save()
        lst.append(author.first_name)
    return HttpResponse(f'{lst}')

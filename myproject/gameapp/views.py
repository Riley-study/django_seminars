from django.shortcuts import render
from django.http import HttpResponse
import random
import logging


# Create your views here.

def index(request):
    return HttpResponse('Hello world!!')


def heads_or_tails(request):
    return HttpResponse(f'{random.choice(["Орел", "Решка"])}')


def cube(request):
    return HttpResponse(f'{random.randint(1, 6)}')


def numbers(request):
    return HttpResponse(f'{random.randint(1, 100)}')

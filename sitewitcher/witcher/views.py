from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse('Страница приложения witcher')


def categories(request):
    return HttpResponse('<h1>Ведьмачьи школы</h1>')
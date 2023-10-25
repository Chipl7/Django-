from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse('Страница приложения witcher')


def categories(request, witcher_school_id):
    return HttpResponse(f'<h1>Ведьмачьи школы</h1><p>id: {witcher_school_id}</p>')


def categories_by_slug(request, witcher_school_slug):
    return HttpResponse(f'<h1>Ведьмачьи школы</h1><p>slug: {witcher_school_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')
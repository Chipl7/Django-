from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):  # HttpRequest
    return HttpResponse('Страница приложения witcher')


def categories(request, witcher_school_id):
    return HttpResponse(f'<h1>Ведьмачьи школы</h1><p>id: {witcher_school_id}</p>')


def categories_by_slug(request, witcher_school_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Ведьмачьи школы</h1><p>slug: {witcher_school_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('school', args=('school', ))
        return redirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

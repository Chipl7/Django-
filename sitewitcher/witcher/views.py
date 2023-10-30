from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ['о сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class Myclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):  # HttpRequest
    # t = render_to_string('witcher/index.html')
    # return HttpResponse(t)
    data = {
            'title': 'Главная страница',
            'menu': menu,
            'float': 28.56,
            'lst': [1, 2, 'abc', True],
            'set': {1, 2, 3, 2, 5},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': Myclass(10, 20)
            }
    return render(request, 'witcher/index.html', context = data)


def about(request):
    return render(request, 'witcher/about.html', {'title': 'О сайте'})


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

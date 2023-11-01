from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Геральт из Ривии', 'content': 'Биография Геральта', 'is_published': True},
    {'id': 2, 'title': 'Йеннифэр из Венгерберга', 'content': 'Биография Йеннифэр', 'is_published': False},
    {'id': 3, 'title': 'Цирилла Фиона Элен Рианнон', 'content': 'Биография Аире', 'is_published': True},
          ]


def index(request):  # HttpRequest
    # t = render_to_string('witcher/index.html')
    # return HttpResponse(t)
    data = {
            'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, 'witcher/index.html', context = data)


def about(request):
    return render(request, 'witcher/about.html', {'title': 'О сайте'})


def show_post(request, post_id):
    return HttpResponse(f'Отображать статью с id = {post_id}')


def addpage(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

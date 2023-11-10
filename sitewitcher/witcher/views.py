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
    {'id': 1, 'title': 'Геральт из Ривии', 'content': '''<h1>Геральт из Ривии</h1>прозванный Белым Волком и Мясником из Блавикена (ориг. Geralt z Rivii) — главный герой литературной саги и протагонист последующих игр, ведьмак из Школы Волка, профессиональный охотник на монстров, один из лучших фехтовальщиков Севера.
    Имеет романтический интерес к двум чародейкам: Йеннифэр из Венгерберга и Трисс Меригольд. Его лучшими друзьями помимо ведьмаков из своей школы являются бард по имени Лютик, краснолюд Золтан Хивай и высший вампир Эмиель Регис.''', 'is_published': True},
    {'id': 2, 'title': 'Йеннифэр из Венгерберга', 'content': 'Биография Йеннифэр', 'is_published': False},
    {'id': 3, 'title': 'Цирилла Фиона Элен Рианнон', 'content': 'Биография Аире', 'is_published': True},
]

character_db = [
    {'id': 1, 'name': 'Ведьмаки'},
    {'id': 2, 'name': 'Волшебницы'},
    {'id': 3, 'name': 'Правители'},
]


def index(request):  # HttpRequest
    # t = render_to_string('witcher/index.html')
    # return HttpResponse(t)
    data = {
            'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            'character_selected': 0,
            }
    return render(request, 'witcher/index.html', context = data)


def about(request):
    return render(request, 'witcher/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Отображать статью с id = {post_id}')


def addpage(request):
    return render(request, 'witcher/addpage.html', {'title': 'Добавить страницу', 'menu': menu})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, character_id):
    data = {
            'title': 'Отображение по рубликам',
            'menu': menu,
            'posts': data_db,
            'character_selected': character_id,
            }
    return render(request, 'witcher/index.html', context = data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

bar = [
    {'title': 'News', 'url_name': 'news'},
    {'title': 'Friends', 'url_name': 'friends'},
    {'title': 'Account', 'url_name': 'account'},

]

data_db = [
    {'id': 1, 'name': 'Василий Пупкинов', 'content': 'Страница Василия Пупкина', 'is_friend': True},
    {'id': 2, 'name': 'Стасян Голубок', 'content': 'Страница Стасяна Голубок', 'is_friend': False},
    {'id': 3, 'name': 'Дымок Чёкавоизачем', 'content': 'Страница Дымок Чёкавоизачем', 'is_friend': True},
]


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def menu(request):
    data = {
        'title': 'Основная страница представления',
        'bar': bar,
    }
    return render(request,
                  'menu/home.html',
                  data)


def show_friend(request, friend_id):
    return HttpResponse(f'Отображение друга с id = {friend_id}')


def show_friends(request):
    data = {
        'title': 'Друзья и подписчики',
        'bar': bar,
        'friends': data_db,
    }
    return render(request,
                  'menu/friends.html',
                  data)


def news(request):
    data = {
        'title': 'Страница с новостями',
        'bar': bar,
    }
    return render(request,
                  'menu/news.html',
                  data)


def account(request):
    return HttpResponse(f'Твой аккаунт')


def readme(request):
    data = {
        'title': 'Как я понял задание?',
        'bar': bar,
    }
    return render(request,
                  'menu/readme.html',
                  data)

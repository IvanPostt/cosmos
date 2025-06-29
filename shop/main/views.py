from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title': 'Информация о сайте', 'url_name': 'about'},
        {'title': 'Контактная информация', 'url_name': 'contact'},
        {'title': 'Создать запись', 'url_name': 'createpost'},
        {'title': 'Вход', 'url_name': 'login'}]


data_db = [{'id': 1, 'title': 'Земля', 'content': 'Информация о Земле', 'is_pub': True},
           {'id': 2, 'title': 'Марс', 'content': 'Информация о Марсе', 'is_pub': False},
           {'id': 2, 'title': 'Венера', 'content': 'Информация о Венере', 'is_pub': True}
           ]


def index(request):
    # t = render_to_string('index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Home',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    return render(request, 'main/about.html', {'title': 'About page', 'menu': menu})


def createpost(request):
    return HttpResponse('Создать запись')

def contact(request):
    return HttpResponse('Контактная информация')

def login(request):
    return HttpResponse('Вход')

def show_post(request, id):
    return HttpResponse(f'id = {id}')



def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")

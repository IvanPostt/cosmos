from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from .models import SpaceObj

menu = [{'title': 'Информация о сайте', 'url_name': 'about'},
        {'title': 'Контактная информация', 'url_name': 'contact'},
        {'title': 'Создать запись', 'url_name': 'createpost'},
        {'title': 'Вход', 'url_name': 'login'}]


cats_db = [{'id': 1, 'title': 'Газовые гиганты'},
           {'id': 2, 'title': 'Звезды'},
           {'id': 3, 'title': 'Каменистые планеты'},
           ]


def index(request):
    posts = SpaceObj.objects.all()
    data = {
        'title': 'Home',
        'menu': menu,
        'posts': posts,
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


def show_post(request, p_slug):
    post = get_object_or_404(SpaceObj, slug=p_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
    }
    return render(request, 'main/posts.html', data)


def show_category(request, category_id):
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from .models import SpaceObj, Category, TagsSpace

menu = [{'title': 'Информация о сайте', 'url_name': 'about'},
        {'title': 'Контактная информация', 'url_name': 'contact'},
        {'title': 'Создать запись', 'url_name': 'createpost'},
        {'title': 'Вход', 'url_name': 'login'}]


def index(request):
    posts = SpaceObj.objects.all()
    categories = Category.objects.all()
    data = {
        'title': 'Home',
        'menu': menu,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    categories = Category.objects.all()
    return render(request, 'main/about.html', {'title': 'About page', 'menu': menu, 'categories': categories})


def createpost(request):
    return HttpResponse('Создать запись')


def contact(request):
    return HttpResponse('Контактная информация')


def login(request):
    return HttpResponse('Вход')


def show_post(request, p_slug):
    post = get_object_or_404(SpaceObj, slug=p_slug)
    categories = Category.objects.all()
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'categories': categories
    }
    return render(request, 'main/posts.html', data)


def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()
    posts = SpaceObj.objects.filter(category=category.id)
    data = {
        'title': f'{category.name}',
        'menu': menu,
        'posts': posts,
        'category': category,
        'categories': categories
    }
    return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")

def show_tags(request, tags_slug):
    tags = get_object_or_404(TagsSpace, slug=tags_slug)
    data = {
        'title': {tags.names},
        'menu': menu,
    }
    return render(request, 'main/index.html', context=data)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import FormView, UpdateView

# from django.views.generic import TemplateView

from .forms import AddForm
from .models import SpaceObj, Category, TagsSpace

menu = [{'title': 'Язык', 'url_name': 'about'},
        {'title': 'Онлайн магазин', 'url_name': 'contact'},
        {'title': 'Создать запись', 'url_name': 'createpost'},
        {'title': 'Вход', 'url_name': 'login'}]


def index(request):
    posts = SpaceObj.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    data = {
        'title': 'Иформация о космичесских объектов.',
        'menu': menu,
        'categories': categories,
        'page_obj': page_obj
    }
    return render(request, 'main/index.html', context=data)




def about(request):
    categories = Category.objects.all()
    return render(request, 'main/about.html', {'title': 'Данные сайта', 'menu': menu, 'categories': categories})

class CreatePost(LoginRequiredMixin, FormView):
    form_class = AddForm
    template_name = 'main/create.html'
    success_url = reverse_lazy('index')

    extra_context = {
        'menu': menu,
        'title': 'Cоздать новую запись',
        'categories': Category.objects.all()
    }
    def dispatch(self, request, *args, **kwargs):
        if request.user.username != 'qq':
            return render(request, 'main/sorry.html', {'error': 'Доступ запрещён: только для администраторов'})
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    model = SpaceObj
    form_class = AddForm
    template_name = 'main/edit.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'menu': menu,
        'title': 'Редактирование Поста',
        'categories':Category.objects.all()
    }

# def edit_post(request, pk):
#     post = get_object_or_404(SpaceObj, pk=pk)
#     if request.method == 'POST':
#         form = AddForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = AddForm(instance=post)
#     return render(request, 'main/edit.html',
#                   {'form': form, 'title': 'Редактирование поста', 'menu': menu, 'categories': Category.objects.all()})




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

    posts_list = SpaceObj.objects.filter(category=category.id)

    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'title': f'{category.name}',
        'menu': menu,
        'categories': categories,
        'page_obj': page_obj,
        'category': category,
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

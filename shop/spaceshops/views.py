from django.shortcuts import render
from .models import SpaceProduct, CategoryObj

menu = [{'title': 'Язык', 'url_name': 'about'},
        {'title': 'Онлайн магазин', 'url_name': 'contact'},
        {'title': 'Вход', 'url_name': 'login'}]
# Create your views here.
def space_shop(request):
    sp = SpaceProduct.objects.all()
    l = CategoryObj.objects.all()
    data = {
        'space': sp,
        'cat': l,
        'menu': menu
    }
    return render(request, 'spaceshops/index.html', context=data)
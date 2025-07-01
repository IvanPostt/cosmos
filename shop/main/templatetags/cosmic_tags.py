from django import template
import main.views as views

from main.models import Category, TagsSpace

register = template.Library()



@register.inclusion_tag('main/list_cat.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('main/list_tags.html')
def show_tags():
    return {'tags': TagsSpace.objects.all()}
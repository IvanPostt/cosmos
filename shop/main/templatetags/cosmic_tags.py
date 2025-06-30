from django import template
import main.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('main/list_cat.html')
def show_categories():
    cats = views.cats_db
    return {'cats': cats}
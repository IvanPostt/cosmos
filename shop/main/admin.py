from django.contrib import admin
from .models import SpaceObj, Category


@admin.register(SpaceObj)
class SpaceAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )
    filter_horizontal = ('tags', )
    list_display = ('title', 'time_created', 'public', 'description', 'category')
    ordering = ('title', )
    list_filter = ('title', 'category')
    list_per_page = 15
    search_fields = ('title', 'category__name')



@admin.register(Category)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name', )

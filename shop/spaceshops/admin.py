from django.contrib import admin
from .models import SpaceProduct, CategoryObj


@admin.register(SpaceProduct)
class SpaceAdmin(admin.ModelAdmin):
    readonly_fields = ('name', )
    list_display = ('name', 'description', 'category')
    ordering = ('name', )
    list_filter = ('name', 'category')
    list_per_page = 15
    search_fields = ('name', 'category__name')



@admin.register(CategoryObj)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ('name', )
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('createpost/', views.createpost, name='createpost'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:p_slug>', views.show_post, name='post'),
    path('category/<slug:category_slug>', views.show_category, name='category'),
    path('tags/<slug:tag_slug>', views.show_tags, name='tags'),
    path('edit/<int:pk>', views.edit_post, name='edit')
]

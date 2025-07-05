from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('createpost/', views.CreatePost.as_view(), name='createpost'),
    path('post/<slug:p_slug>', views.show_post, name='post'),
    path('category/<slug:category_slug>', views.show_category, name='category'),
    path('tags/<slug:tag_slug>', views.show_tags, name='tags'),
    path('edit/<slug:slug>', views.EditPost.as_view(), name='edit')
]

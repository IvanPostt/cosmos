from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('createpost/', views.createpost, name='createpost'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:p_slug>', views.show_post, name='post'),
    path('category/<int:category_id>', views.show_category, name='category')
]

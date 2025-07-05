from django.urls import path
from . import views

app_name = 'spaceshops'  # ОБЯЗАТЕЛЬНО!

urlpatterns = [
    path('space/', views.space_shop, name='contact'),
]
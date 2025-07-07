from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<int:pk>', views.ProfileUser.as_view(), name='profile'),
    path('password_change/', views.password_change, name='password_change')
]

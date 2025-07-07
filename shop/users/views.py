from django.contrib.auth import authenticate, login as auth_login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from django.contrib import messages
from .forms import UserForm, RegistrationForm, ProfileForm


class LoginView(LoginView):
    form_class = UserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('index')
# def user_login(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 auth_login(request, user)
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserForm()
#     return render(request, 'users/login.html', {'form': form})
def user_logout(request):
     logout(request)
     return render(request, 'users/logout.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('users:login'))
    else:
        form = RegistrationForm()
    return render(request, 'users/registrations.html', {'form': form})

class ProfileUser(LoginRequiredMixin, UpdateView):
    mode = get_user_model()
    form_class = ProfileForm
    template_name = 'users/profile.html'
    extra_context = {'title': 'Профиль'}
    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])

    def get_object(self, queryset=None):
        return self.request.user

def password_change(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password == confirm_password:
            try:
                user = get_user_model().objects.get(username=username)
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect(reverse('users:login'))
            except get_user_model().DoesNotExist:
                messages.error(request, 'Такой пользователь не существует')
        else:
            messages.error(request, 'Пароли не совпадают')
    else:
        return render(request, 'users/change_password.html')

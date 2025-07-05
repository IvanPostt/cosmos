from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserForm


def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserForm()
    return render(request, 'users/login.html', {'form': form})
def logout(request):
    return HttpResponse("Выход")
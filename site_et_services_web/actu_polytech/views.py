from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import  User
from django.contrib.auth.decorators import login_required
from news.models import Article, Category

from . import forms

# Create your views here.
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'actu_polytech/signup.html', context={'form': form})

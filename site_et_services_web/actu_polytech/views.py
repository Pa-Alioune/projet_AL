from django.conf import settings
import os
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import  User
from django.contrib.auth.decorators import login_required
from news.models import Article, Category

from . import forms
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from actu_polytech.soap import SOAPHandler

@csrf_exempt
def soap_view(request):
    handler = SOAPHandler(request)
    if request.method == 'GET':
        return handler.soap_GET()
    elif request.method == 'POST':
        return handler.soap_POST()
    
@csrf_exempt
def wsdl_view(request):
    # Chemin vers le fichier WSDL
    wsdl_file_path = os.path.join(settings.BASE_DIR, 'actu_polytech', 'wsdl', 'my_service.wsdl')
    
    # Lisez le contenu du fichier WSDL
    with open(wsdl_file_path, 'rb') as wsdl_file:
        wsdl_content = wsdl_file.read()

    # Renvoyez le contenu du fichier WSDL comme réponse HTTP
    return HttpResponse(wsdl_content, content_type='text/xml')    

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

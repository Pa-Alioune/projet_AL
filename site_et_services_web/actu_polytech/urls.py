from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)

# app_name = 'actu_polytech'
urlpatterns = [
  path('login/', LoginView.as_view(
        template_name='actu_polytech/login.html',
        redirect_authenticated_user=True),
         name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('signup/', views.signup_page, name='signup'),
]

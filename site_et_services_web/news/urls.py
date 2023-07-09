from django.urls import path
from . import views

# app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),


    path('manage-articles/', views.manage_articles, name='manage_articles'),
    path('manage-articles/<int:article_id>/', views.manage_article, name='manage_article'),
    path('manage-articles/add/', views.add_article, name='add_article'),
    path('manage-articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),


]

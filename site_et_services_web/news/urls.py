from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from news.views import *
from actu_polytech.views import soap_view

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
router.register('articles-categorie', ArticleCategoryViewSet, basename='articles-categorie')

# app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),


    path('manage-articles/', views.manage_articles, name='manage_articles'),
    path('manage-articles/<int:article_id>/', views.manage_article, name='manage_article'),
    path('manage-articles/add/', views.add_article, name='add_article'),
    path('manage-articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),




    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-users/<int:user_id>/', views.manage_user, name='manage_user'),
    path('manage-users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('manage-categories/', views.manage_categories, name='manage_categories'),
    path('manage-categories/<int:category_id>/', views.manage_category, name='manage_category'),
    path('manage-categories/add/', views.add_category, name='add_category'),
    path('manage-categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),



    path('request-token/', RequestTokenView.as_view(), name='request-token'),
    path('manage-tokens/', ManageTokenView.as_view(), name='manage-tokens'),
    path('delete-token/', DeleteTokenView.as_view(), name='delete-token'),


    path('siteadmin/', views.manage_site, name='siteadmin'),


]

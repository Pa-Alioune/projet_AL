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
<<<<<<< HEAD


    path('manage-articles/', views.manage_articles, name='manage_articles'),
    path('manage-articles/<int:article_id>/', views.manage_article, name='manage_article'),
    path('manage-articles/add/', views.add_article, name='add_article'),
    path('manage-articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),


=======
    # path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    # path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('soap/', soap_view, name='soap'), # type: ignore
    path('api/', include(router.urls)),
>>>>>>> 9c7229121b3e771fb4c76be051a34d121413f8ac
]

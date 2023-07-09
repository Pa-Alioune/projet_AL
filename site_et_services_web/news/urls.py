from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from news.views import *
from actu_polytech.views import soap_view

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')
router.register('articles-categorie', ArticleCategoryViewSet, basename='articles-categorie')

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    # path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    # path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('soap/', soap_view, name='soap'), # type: ignore
    path('api/', include(router.urls)),
]

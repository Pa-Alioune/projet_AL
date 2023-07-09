from django.shortcuts import render
from .models import Article, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from news.serializers import *
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from django.http import HttpResponse


def index(request):
    articles = Article.objects.all().order_by('-created_at')
    paginator = Paginator(articles, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/index.html', {'page_obj': page_obj})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'news/article_detail.html', {'article': article})

def category_view(request, category_name):
    articles = Article.objects.filter(category__name=category_name).order_by('-created_at')
    paginator = Paginator(articles, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'news/category.html', {'page_obj': page_obj})

# @login_required
# def edit_article(request, article_id):
    
#     pass

# @login_required
# def delete_article(request, article_id):
   
#     pass

class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:  # type: ignore
            return self.detail_serializer_class
        return super().get_serializer_class()  # type: ignore
    
class ArticleViewSet(MultipleSerializerMixin, ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, XMLRenderer]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        format = request.GET.get('format', 'json')
        if format == 'xml':
            return Response(serializer.data, content_type='application/xml')
        else:
            return Response(serializer.data)
        
class ArticleCategoryViewSet(MultipleSerializerMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [JSONRenderer, XMLRenderer]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        format = request.GET.get('format', 'json')
        if format == 'xml':
            return Response(serializer.data, content_type='application/xml')
        else:
            return Response(serializer.data)        
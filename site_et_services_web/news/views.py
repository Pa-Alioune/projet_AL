from .models import Article, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from news.serializers import *
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from django.http import HttpResponse
from django.views import View
from django.utils import timezone




from django.contrib.auth import get_user_model
import uuid

from django.shortcuts import render, get_object_or_404, redirect
from actu_polytech.models import User


def index(request):
    articles = Article.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    paginator = Paginator(articles, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_time = timezone.now()
    for article in articles:
        article.time_diff = (current_time - article.created_at).total_seconds()

    return render(request, 'news/index.html', {'page_obj': page_obj,'categories': categories,'current_time': current_time})

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'news/article_detail.html', {'article': article})

def category_view(request, category_name):
    categories = Category.objects.all()
    current_time = timezone.now()
    articles = Article.objects.filter(category__name=category_name).order_by('-created_at')
    paginator = Paginator(articles, 5)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for article in articles:
        article.time_diff = (current_time - article.created_at).total_seconds()

    return render(request, 'news/category.html', {'page_obj': page_obj,'categories': categories,'current_time': current_time})

# @login_required
# def edit_article(request, article_id):
    
#     pass

# @login_required
# def delete_article(request, article_id):
   
#     pass
# site_web/views.py
@login_required(login_url='login')
def manage_site(request):
    if request.user.role in ['editor', 'admin']:
        
        return render(request, 'news/admin.html', )
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def manage_articles(request):
    if request.user.role in ['editor', 'admin']:
        articles = Article.objects.all()
        return render(request, 'news/manage_articles.html', {'articles': articles})
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def manage_article(request, article_id):
    if request.user.role in ['editor', 'admin']:
        article = get_object_or_404(Article, id=article_id)
        if request.method == 'POST':
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.category = get_object_or_404(Category, id=request.POST.get('category_id'))
            article.save()
            return redirect('manage_articles')
        else:
            categories = Category.objects.all()
            return render(request, 'news/manage_article.html', {'article': article, 'categories': categories})

@login_required(login_url='login')
def add_article(request):
    if request.user.role in ['editor', 'admin']:
        if request.method == 'POST':
            title = request.POST.get('title')
            content = request.POST.get('content')
            category_id = request.POST.get('category_id')
            category = get_object_or_404(Category, id=category_id)
           
            article = Article.objects.create(title=title, content=content, category=category, author=request.user)
            return redirect('manage_articles')
        else:
            categories = Category.objects.all()
            return render(request, 'news/add_article.html', {'categories': categories})
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def delete_article(request, article_id):
    if request.user.role in ['editor', 'admin']:
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('manage_articles')
    else:
        return render(request, 'news/unauthorized.html')
    
########gestiin utilisateur et categorie    

@login_required(login_url='login')
def manage_users(request):
    if request.user.role == 'admin':
        users = User.objects.all()
        return render(request, 'news/manage_users.html', {'users': users})
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def manage_user(request, user_id):
    if request.user.role == 'admin':
        user = get_object_or_404(User, id=user_id)
        if request.method == 'POST':
            user.username = request.POST.get('username')
            user.email = request.POST.get('email')
            user.save()
            return redirect('manage_users')
        else:
            return render(request, 'news/manage_user.html', {'user': user})

@login_required(login_url='login')
def delete_user(request, user_id):
    if request.user.role == 'admin':
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return redirect('manage_users')
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def manage_categories(request):
    if request.user.role in ['editor', 'admin']:
        categories = Category.objects.all()
        return render(request, 'news/manage_categories.html', {'categories': categories})
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def manage_category(request, category_id):
    if request.user.role in ['editor', 'admin']:
        category = get_object_or_404(Category, id=category_id)
        if request.method == 'POST':
            category.name = request.POST.get('name')
            category.save()
            return redirect('manage_categories')
        else:
            return render(request, 'news/manage_category.html', {'category': category})

@login_required(login_url='login')
def add_category(request):
    if request.user.role in ['editor', 'admin']:
        if request.method == 'POST':
            name = request.POST.get('name')
            category = Category.objects.create(name=name)
            return redirect('manage_categories')
        else:
            return render(request, 'news/add_category.html')
    else:
        return render(request, 'news/unauthorized.html')

@login_required(login_url='login')
def delete_category(request, category_id):
    if request.user.role in ['editor', 'admin']:
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('manage_categories')
    else:
        return render(request, 'news/unauthorized.html')






##### gestion Token 

class ManageTokenView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.role == 'admin':
            token_requests = get_user_model().objects.filter(token_requested=True)
            return render(request, 'news/manage_tokens.html', {'token_requests': token_requests})
        else:
            return render(request, 'news/unauthorized.html')

    def post(self, request):
        if request.user.is_authenticated and request.user.role == 'admin':
            action = request.POST.get('action')
            user_id = request.POST.get('user_id')
            user = get_user_model().objects.get(id=user_id)
            if action == 'generate':
                user.token = uuid.uuid4()
                user.token_requested = True
                user.save()
            elif action == 'delete':
                user.token = None
                user.token_requested = True
                user.save()
            return redirect('manage-tokens')
        else:
            return render(request, 'news/unauthorized.html')
        

class DeleteTokenView(View):
    def post(self, request):
        if request.user.is_authenticated and request.user.role == 'admin':
            user_id = request.POST.get('user_id')
            user = get_user_model().objects.get(id=user_id)
            user.token = None
            user.save()
            return HttpResponse("Token deleted.")
        else:
            return render(request, 'news/unauthorized.html')



class RequestTokenView(View):
    def get(self, request):
        if request.user.is_authenticated:
            request.user.token_requested = True
            request.user.save()
            return render(request, 'news/token.html')
        else:
            return render(request, 'news/unauthorized.html')






























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

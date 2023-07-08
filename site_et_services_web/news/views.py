from django.shortcuts import render
from .models import Article, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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

@login_required
def edit_article(request, article_id):
    
    pass

@login_required
def delete_article(request, article_id):
   
    pass

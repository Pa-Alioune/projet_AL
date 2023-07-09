from .models import Article, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404, redirect
from actu_polytech.models import User


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
# site_web/views.py

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
            article = Article.objects.create(title=title, content=content, category=category)
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


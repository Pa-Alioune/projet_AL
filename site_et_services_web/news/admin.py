from django.contrib import admin
from news.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'category', 'author')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
<<<<<<< HEAD
from .models import Article, Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article)
admin.site.register(Category)
=======
from news.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'category', 'author')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')   
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
>>>>>>> 9c7229121b3e771fb4c76be051a34d121413f8ac

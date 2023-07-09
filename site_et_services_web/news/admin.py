from django.contrib import admin
from .models import Article, Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Article)
admin.site.register(Category)

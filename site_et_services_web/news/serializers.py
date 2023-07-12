from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        
class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'articles']        
        
    def get_articles(self, instance):
        queryset = instance.articles.all()
        serializer = ArticleSerializer(queryset, many=True) 
        return serializer.data   
from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.urls import reverse
import json
from .models import Article, Category, Author

# Create your views here.
def articles(request):
    articles = Article.objects.all()
    
    return render(request, 'content/articles.html', {'articles': articles})

def article(request, id):
    article = Article.objects.get(id=id)
    
    return render(request, 'content/article.html', {'article': article})

def category(request, id):
    category = Category.objects.get(id=id)

    articles = category.articles.all()

    
    return render(request, 'content/category.html', {'category':category, 'articles': articles})

def author(request, id):
    author = Author.objects.get(id=id)
    articles = author.articles.all()

    return render(request, 'content/author.html', {'author': author, 'articles': articles})
    
from django.shortcuts import render
from .models import Game, Category, Author


def game(request, id):
    game = Game.objects.get(id=id)
    
    return render(request, 'content/game.html', {'game': game})

def games(request):
    games = Game.objects.all()
    
    return render(request, 'content/games.html', {'games': games})


def category(request, id):
    category = Category.objects.get(id=id)

    games = category.games.all()

    
    return render(request, 'content/category.html', {'category':category, 'games': games})

def categories(request):
    categories = Category.objects.all()
    
    return render(request, 'content/categories.html', {'categories': categories})

def author(request, id):
    author = Author.objects.get(id=id)
    games = author.games.all()

    return render(request, 'content/author.html', {'author': author, 'games': games})

def authors(request):
    authors = Author.objects.all()
    
    return render(request, 'content/authors.html', {'authors': authors})


def homepage(request):
    games = Game.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    return render(request, 'content/homepage.html', {'games': games, 'categories': categories, 'authors': authors})

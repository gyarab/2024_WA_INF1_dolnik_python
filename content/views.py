from django.shortcuts import render
from .models import Game, Category, Author

def games(request):
    games = Game.objects.all()
    
    return render(request, 'content/games.html', {'games': games})

def categories(request):
    categories = Category.objects.all()
    
    return render(request, 'content/categories.html', {'categories': categories})

def game(request, id):
    game = Game.objects.get(id=id)
    
    return render(request, 'content/game.html', {'game': game})

def category(request, id):
    category = Category.objects.get(id=id)

    games = category.games.all()

    
    return render(request, 'content/category.html', {'category':category, 'games': games})

def author(request, id):
    author = Author.objects.get(id=id)
    games = author.games.all()

    return render(request, 'content/author.html', {'author': author, 'games': games})

def homepage(request):
    games = Game.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    return render(request, 'content/homepage.html', {'games': games, 'categories': categories, 'authors': authors})
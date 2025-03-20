from django.shortcuts import render
from .models import Game, Category, Author, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm



def game(request, id):
    game = Game.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            comment = Comment()
            comment.name = data['name']
            comment.text = data['text']
            comment.game = game
            comment.ip = request.META.get('REMOTE_ADDR')
            comment.user_agent = request.META.get('HTTP_USER_AGENT')
            comment.save()
            return HttpResponseRedirect(reverse('content:game', args=[id]))
    if request.method == 'GET':
      
        if 'voted_games' not in request.COOKIES:
            game.votes_sum += int(request.GET.get('vote', 0))
            game.votes_count += 1
            game.save()
            response = HttpResponseRedirect(reverse('content:game', args=[id]))
            response.set_cookie('voted_games', str(game.id))
            return response
        game.save()

    return render(request, 'content/game.html', {'game': game, 'form': form})

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

from django.shortcuts import render
from .models import Game, Category, Author, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm, LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.shortcuts import redirect


def game(request, id):
    game = Game.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            comment = Comment()
            if request.user.is_authenticated:
                comment.name = request.user.username
            else:
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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('content:homepage'))
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'content/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return HttpResponseRedirect(reverse('content:login'))
    else:
        form = RegistrationForm()
    return render(request, 'content/register.html', {'form': form})



@require_POST
def logout_view(request):
    logout(request)
    return redirect('/')
    
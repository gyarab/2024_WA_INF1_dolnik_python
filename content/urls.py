from django.urls import path
from .views import games, game, category, author, categories, homepage, authors

app_name = 'content'

urlpatterns = [
    path('games/', games, name='games'),
    path('', homepage, name='homepage'),
    path('game/<int:id>/',game, name='game'),
    path('category/<int:id>/', category, name='category'),
    path('categories/', categories, name='categories'),
    path('author/<int:id>/', author, name='author'),
    path('authors/', authors, name='authors'),
]
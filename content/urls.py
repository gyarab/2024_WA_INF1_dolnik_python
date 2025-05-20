from django.urls import path
from .views import games, game, category, author, categories, homepage, authors, login_view, register, logout_view

app_name = 'content'

urlpatterns = [
    path('games/', games, name='games'),
    path('', homepage, name='homepage'),
    path('game/<int:id>/',game, name='game'),
    path('category/<int:id>/', category, name='category'),
    path('categories/', categories, name='categories'),
    path('author/<int:id>/', author, name='author'),
    path('authors/', authors, name='authors'),
    path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
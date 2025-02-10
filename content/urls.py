from django.urls import path
from .views import articles, article, category, author

app_name = 'content'

urlpatterns = [
    path('', articles, name='articles'),
    path('game/<int:id>/', article, name='article'),
    path('category/<int:id>/', category, name='category'),
    path('author/<int:id>/', author, name='authors'),
]
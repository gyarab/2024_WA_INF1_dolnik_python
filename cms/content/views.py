from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
import json

def hello_world(request):
    return HTTPResponse("Hello World")
def load_articles(request):
    with open('articles.json', encoding="utf-8") as f:
        articles = json.load(f)   
        
        html_list ='<ul>'
        for article in articles:
            title = article['title']
            html_list += f'<li>{title}</li>'
        html_list += '</ul>'
    return HTTPResponse(html_list)


# Create your views here.

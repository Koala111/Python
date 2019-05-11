from django.shortcuts import render
from django.http import HttpResponse
import time
from blog.models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def article_page(request, article_id):
    article = Article.objects.get(article_id)
    return render(request, 'article_page.html', {'article': article})

def login(request):
    return render(request , 'login.html', {'name': 'daixiong'})
def quit(request):

    return render(request, 'quit.html', {'time': time.ctime})
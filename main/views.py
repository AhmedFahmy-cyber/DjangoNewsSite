from django.shortcuts import render
from .models import News , Category ,Comment
from django.contrib import messages
import datetime
# Create your views here.


def home(request):

    first_news=News.objects.first()
    side_news=News.objects.all()[1:4]
    three_categories=Category.objects.all()
    context = {
        'three_categories':three_categories,
        'side_news':side_news,
        'first_news':first_news ,
    }

    return render (request  , 'main/home.html' ,context )

def all_news(request):
    allnews=News.objects.all()
    return render (request  , 'main/all-news.html' ,{
        'allnews':allnews , 
    })

def detailnews(request , id):
    

    news = News.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        
        Comment.objects.create(
            news=news,
            name=name,
            email = email ,
            comment=comment,
            
        )
        
        messages.success(request , 'comment has benn submitted but in moderation mode')
    category = Category.objects.get(id=news.category.id)
    related_news=News.objects.filter(category=category).exclude(id=id)
    comments = Comment.objects.filter(news=news,status=True ).order_by('-id')

    return render (request , 'main/detail.html' , 
    
    {'news':news,
    'related_news':related_news,
    'category':category,
    'comments':comments,
    })
    
def all_category(request):
    cats = Category.objects.all()
    return render (request , 'main/category.html' , {
        
        'cats' : cats , 
    })
        

def category(request,id):
    
    category = Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render (request , 'main/category-news.html' , {
        
        'all_news' : news , 
        'category' : category ,
    })        
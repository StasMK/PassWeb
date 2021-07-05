from django.shortcuts import render
from .models import Articles


# Create your views here.
def news_home(request):
    news = Articles.objects.all()
    return render(request,'news/news.html', {'news':news})

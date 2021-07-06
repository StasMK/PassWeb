from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# Create your views here.
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news.html', {'news': news})


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()
    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)

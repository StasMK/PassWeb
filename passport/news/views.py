from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    # fields = ['troad', 'nroad', 'n_km', 'k_km']

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'

    # form_class = ArticlesForm
    # fields = ['troad', 'nroad', 'n_km', 'k_km']

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

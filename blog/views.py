from django.views import generic
from .models import Author, Article

class IndexView(generic.ListView):

    template_name = 'blog/IndexView.html'

    def get_queryset(self):
        return Article.objects.all()

class DetailView(generic.DetailView):

    template_name = 'blog/DetailView.html'
    model = Article
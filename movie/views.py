from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView
from .models import Movie , MovieLinks

class MovieList(ListView):
    model = Movie
    paginate_by = 1
class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail,self).get_object()
        object.views_count += 1
        object.save()
        return object
    def get_context_data(self , **kwargs):
        context = super(MovieDetail,self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context
    
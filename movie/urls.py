from django.urls import path
from .views import MovieDetail , MovieList , MovieCategory

app_name = 'movie'

urlpatterns = [
    path('<int:pk>', MovieDetail.as_view() , name='movie_detail'),
    path('', MovieList.as_view() , name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view() , name='movie_category'),
]

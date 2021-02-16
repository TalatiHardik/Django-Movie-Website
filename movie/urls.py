from django.urls import path
from .views import MovieDetail , MovieList


urlpatterns = [
    path('<int:pk>', MovieDetail.as_view() , name='movie_detail'),
    path('', MovieList.as_view() , name='movie_list'),
]

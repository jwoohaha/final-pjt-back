from django.urls import path
from movies import views

urlpatterns = [
    path('movies_rating_top20/', views.movie_list),
    path('movies/<int:movie_pk>', views.movie_detail),
]
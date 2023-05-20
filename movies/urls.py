from django.urls import path
from movies import views

urlpatterns = [
    path('popular/', views.movie_list_popular),
    path('rating_top20/', views.movie_list_top20),
    path('<int:movie_pk>/', views.movie_detail),
]
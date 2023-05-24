from django.urls import path
from movies import views

urlpatterns = [
    path('popular/', views.movie_list_popular),
    path('rating_top20/', views.movie_list_top20),
    path('<int:movie_pk>/', views.movie_detail),
    path('<str:search_string>/', views.movie_search),
    path('recommend/<int:user_pk>/', views.movie_recommend),
    path('recommend/<int:user1_pk>/<int:user2_pk>/', views.movie_recommend_mixed),
]
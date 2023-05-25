from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update/', views.update_user),
    path('get_user_id/', views.get_user_id),
]


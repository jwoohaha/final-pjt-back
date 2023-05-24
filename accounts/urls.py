from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('update/', views.update_user),
]

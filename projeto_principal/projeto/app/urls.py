from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_list, name='anime_lista'),
]
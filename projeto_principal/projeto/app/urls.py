from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_list, name='anime_list'),
    path('favoritos/', views.favorites, name='favoritos'),
    path('add-favorito/<int:mal_id>/', views.add_favorite, name='add_favorito'),
    path('delete-favorito/<int:pk>/', views.delete_favorite, name='delete_favorito'),
]

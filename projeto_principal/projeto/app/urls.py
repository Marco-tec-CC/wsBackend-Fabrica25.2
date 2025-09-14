from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_list, name='anime_list'),
    path('favoritos/', views.favorites, name='favoritos'),
    path('add-favorito/<int:mal_id>/', views.add_favorite, name='add_favorito'),
    path('edit-favorito/<int:pk>/', views.edit_favorite, name='edit_favorito'),  # rota de edição
    path('delete-favorito/<int:pk>/', views.delete_favorite, name='delete_favorito'),
    path("add_favorito/", views.add_favorito, name="add_favorito"),
]

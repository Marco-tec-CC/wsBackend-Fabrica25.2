import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime

#Aqui pega algumas informações na prorpia API jikan

def anime_list(request):
    query = request.GET.get('q', 'naruto')  # padrão
    url = f'https://api.jikan.moe/v4/anime?q={query}&limit=10'

    response = requests.get(url)
    data = response.json()
    animes = []

    if 'data' in data:
        for item in data['data']:
            animes.append({
                'mal_id': item['mal_id'],
                'title': item['title'],
                'image_url': item['images']['jpg']['image_url'],
                'synopsis': item['synopsis'],
            })

    return render(request, 'anime_base.html', {'animes': animes})


# Adicionando favorito :D

def add_favorite(request, mal_id):
    url = f'https://api.jikan.moe/v4/anime/{mal_id}'
    response = requests.get(url)
    data = response.json()

    if 'data' in data:
        anime_data = data['data']
        Anime.objects.get_or_create(
            mal_id=anime_data['mal_id'],
            defaults={
                'title': anime_data['title'],
                'image_url': anime_data['images']['jpg']['image_url'],
                'synopsis': anime_data['synopsis'] or "Sem descrição"
            }
        )
    return redirect('favoritos')


# Listar os favoritos 


def favorites(request):
    favoritos = Anime.objects.all()
    return render(request, 'favoritos.html', {'favoritos': favoritos})


# Remover os favoritos


def delete_favorite(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    anime.delete()
    return redirect('favoritos')

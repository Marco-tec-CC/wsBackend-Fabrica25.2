import requests
from django.shortcuts import render

def anime_list(request):
    query = request.GET.get('q', 'naruto')  # pesquisa padrão
    url = f'https://api.jikan.moe/v4/anime?q={query}&limit=10'

    response = requests.get(url)
    data = response.json()
    animes = []

    if 'data' in data:
        for item in data['data']:
            animes.append({
                'title': item['title'],
                'image_url': item['images']['jpg']['image_url'],
                'synopsis': item['synopsis'],
            })

    return render(request, 'anime_base.html', {'animes': animes})

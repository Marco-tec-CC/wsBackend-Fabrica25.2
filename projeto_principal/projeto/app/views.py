import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Anime, Categoria
from .forms import AnimeForm  # vamos usar para edição


# Buscar animes na API Jikan
def anime_list(request):
    query = request.GET.get("q", "naruto")  # valor padrão
    url = f"https://api.jikan.moe/v4/anime?q={query}&limit=10"
    response = requests.get(url).json()

    animes = []
    if "data" in response:
        for anime in response["data"]:
            animes.append({
                "mal_id": anime["mal_id"],
                "title": anime["title"],
                "image_url": anime["images"]["jpg"]["image_url"],
                "synopsis": anime.get("synopsis", "Sem descrição disponível.")
            })

    categorias = Categoria.objects.all()

    return render(request, "anime_base.html", {
        "animes": animes,
        "categorias": categorias
    })
# Criar (adicionar favorito)
def add_favorite(request, mal_id):
    url = f'https://api.jikan.moe/v4/anime/{mal_id}'
    response = requests.get(url)
    data = response.json()

    categoria_id = request.POST.get('categoria_id')  # <-- captura categoria
    categoria = None
    if categoria_id:
        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            categoria = None

    if 'data' in data:
        anime_data = data['data']
        Anime.objects.get_or_create(
            mal_id=anime_data['mal_id'],
            defaults={
                'title': anime_data['title'],
                'image_url': anime_data['images']['jpg']['image_url'],
                'synopsis': anime_data['synopsis'] or "Sem descrição",
                'categoria': categoria  # <-- salva categoria
            }
        )
    return redirect('favoritos')


# Read (listar favoritos)
def favorites(request):
    favoritos = Anime.objects.all()
    return render(request, 'favoritos.html', {'favoritos': favoritos})


# Update (editar favorito)
def edit_favorite(request, pk):
    anime = get_object_or_404(Anime, pk=pk)

    if request.method == "POST":
        form = AnimeForm(request.POST, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('favoritos')
    else:
        form = AnimeForm(instance=anime)

    return render(request, 'edit_favorito.html', {'form': form, 'anime': anime})


# Delete (remover favorito)
def delete_favorite(request, pk):
    anime = get_object_or_404(Anime, pk=pk)
    anime.delete()
    return redirect('favoritos')

def add_favorito(request):
    if request.method == "POST":
        mal_id = request.POST.get("mal_id")
        categoria_id = request.POST.get("categoria_id")
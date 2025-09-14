from django import forms
from .models import Anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'synopsis']  # só deixamos editar título e sinopse

from django.views.generic import ListView

from .models import Anagramgame

class AnagramListView(ListView):
    model = Anagramgame
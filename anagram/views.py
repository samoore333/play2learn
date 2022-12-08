from django.views.generic import ListView

from .models import Anagram

class AnagramListView(ListView):
    model = Anagram
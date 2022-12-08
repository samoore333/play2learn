from django.views.generic import ListView

from .models import Mathgame

class MathgameListView(ListView):
    model = Mathgame

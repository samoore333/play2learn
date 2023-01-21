import json
from time import sleep
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Mathgame
from .forms import MathgameForm, MathgamePlayForm

class MathgameCreateView(CreateView):
    model = Mathgame
    form_class = MathgameForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MathgameDetailView(DetailView):
    model = Mathgame

class MathgameListView(LoginRequiredMixin, ListView):
    model = Mathgame
    fields = ['operation', 'max_number']
    paginate_by = 10
    ordering = ['score']

class MathgameUpdateView(UpdateView):
    model = Mathgame
    form_class = MathgamePlayForm

def score(request, slug):
    user = request.user 
    mathgame = Mathgame.objects.get(slug=slug)
    data = json.loads(request.body)

    score = data['score']

    mathgame_score = Mathgame(user=user, mathgame=mathgame, score=score)
    mathgame_score.save()
    score += 1

    response = {'score': score}
    return JsonResponse(response)

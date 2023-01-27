import json
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Mathgame, MathgameScore
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
    paginate_by = 10
    ordering = ['-score']

class MathgameUpdateView(UpdateView):
    model = Mathgame
    form_class = MathgamePlayForm

def playerScore(request, slug):
    user = request.user
    mathgame = Mathgame.objects.get(slug=slug)
    data = json.loads(request.body)

    scores = data['scores']

    mathgame_score = MathgameScore(user=user, mathgame=mathgame, scores=scores)
    mathgame_score.save()

    response = {
        'scores': scores,
    }

    return JsonResponse(response)



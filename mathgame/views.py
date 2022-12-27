from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mathgame
from .forms import MathgameForm, MathgamePlay, MathgameScore

class MathgameStartView(CreateView):
    model = Mathgame
    form_class = MathgameForm

class MathgamePlayView(UpdateView):
    model = Mathgame
    form_class = MathgamePlay

class MathgameScoreView(UpdateView):
    model = Mathgame
    form_class = MathgameScore

class MathgameListView(LoginRequiredMixin, ListView):
    model = Mathgame
    fields = ['operation', 'max_number', 'score', 'end_time']
    paginate_by = 10
    ordering = ['score']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MathGameView(TemplateView):
    template_name = 'mathgame/math_facts_practice.html'
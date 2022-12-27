from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mathgame

class MathgameCreateView(CreateView):
    model = Mathgame
    fields = ['operation', 'max_number']

class MathgameUpdateView(UpdateView):
    model = Mathgame
    fields = ['answer', 'end_time', 'score']

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
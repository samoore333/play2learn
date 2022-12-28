from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mathgame
from .forms import MathgameForm

class MathgameCreateView(CreateView):
    model = Mathgame
    fields = ['operation', 'max_number']

class MathgameDetailView(DetailView):
    model = Mathgame

class MathgameListView(LoginRequiredMixin, ListView):
    model = Mathgame
    fields = ['operation', 'max_number', 'score', 'end_time']
    paginate_by = 10
    ordering = ['score']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MathgameUpdateView(UpdateView):
    model = Mathgame
    fields = ['operation', 'score', 'end_time']
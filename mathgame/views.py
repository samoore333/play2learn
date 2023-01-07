import random
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def random_nums(a, b):
    # Get random numbers for game
        if Mathgame.operation == '+':
            a = random.randint(1, [Mathgame.max_number])
            b = random.randint(1, [Mathgame.max_number])
        elif Mathgame.operation == 'x':
            a = random.randint(1, [Mathgame.max_number])
            b = random.randint(1, [Mathgame.max_number])
        elif Mathgame.operation == '-':
            a = random.randint(1, [Mathgame.max_number])
            b = random.randint(1, [Mathgame.max_number])
            if b > a:
                b, a = a, b
        else:
            b = random.randint(1, [Mathgame.max_number])
            c = random.randint(1, [Mathgame.max_number])
            a = b * c
        
        return {a: num1, b
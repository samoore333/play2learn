import random
from django.shortcuts import render
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

def random_nums():
# Get random numbers for game
    if Mathgame.operation == '+':
        num1 = random.randint(1, [Mathgame.max_number])
        num2 = random.randint(1, [Mathgame.max_number])
    elif Mathgame.operation == 'x':
        num1 = random.randint(1, [Mathgame.max_number])
        num2 = random.randint(1, [Mathgame.max_number])
    elif Mathgame.operation == '-':
        num1 = random.randint(1, [Mathgame.max_number])
        num2 = random.randint(1, [Mathgame.max_number])
        if num2 > num1:
            num2, num1 = num1, num2
    else:
        num2 = random.randint(1, [Mathgame.max_number])
        numx = random.randint(1, [Mathgame.max_number])
        num1 = num2 * numx

    return num1 + num2
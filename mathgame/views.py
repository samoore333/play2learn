from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Mathgame

class MathgameListView(LoginRequiredMixin, ListView):
    model = Mathgame
    paginate_by = 10
    ordering = ['score']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MathGameView(TemplateView):
    template_name = 'mathgame/math_facts_practice.html'
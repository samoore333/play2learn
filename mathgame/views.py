from django.views.generic import ListView

from .models import Mathgame

class MathgameListView(ListView):
    model = Mathgame

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

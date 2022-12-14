from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Anagramgame

class AnagramListView(LoginRequiredMixin, ListView):
    model = Anagramgame
    paginate_by = 10
    ordering = ['score']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnagramHuntView(TemplateView):
    template_name = 'anagram/anagram_hunt.html'
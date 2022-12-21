from django.views.generic import ListView

from .models import Anagramgame

class AnagramListView(ListView):
    model = Anagramgame

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
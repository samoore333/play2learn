from django.views.generic import ListView
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anagramgame
from .forms import AnagramgameForm, AnagramgamePlayForm


class AnagramgameCreateView(CreateView):
    model = Anagramgame
    form_class = AnagramgameForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AnagramgameDetailView(DetailView):
    model = Anagramgame

class AnagramgameListView(LoginRequiredMixin, ListView):
    model = Anagramgame
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order_fields, order_key, direction = self.get_order_settings()

        context['order'] = order_key
        context['direction'] = direction
        
        # get all but the last order key, which is 'default'
        context['order_fields'] = list(order_fields.keys())[:-1]

        return context
    
    def get_ordering(self):
        order_fields = self.get_order_fields()
        default_order_key = order_fields['default_key']
        order_key = self.request.GET.get('order', default_order_key)
        direction = self.request.GET.get('direction', 'desc')
        
        # If order_key is invalid, use default
        if order_key not in order_fields:
            order_key = default_order_key
        
        ordering = order_fields[order_key]

        # if direction is 'desc' or is invalid use descending order
        if direction != 'asc':
            ordering = '-' + ordering

        return ordering

    def get_order_settings(self):
        order_fields = self.get_order_fields()
        default_order_key = order_fields['default_key']
        order_key = self.request.GET.get('order', default_order_key)
        direction = self.request.GET.get('direction', 'desc')
        
        # If order_key is invalid, use default
        if order_key not in order_fields:
            order_key = default_order_key

        return (order_fields, order_key, direction)

    
    def get_order_fields(self):
        # Returns a dict mapping friendly names to field names and lookups.
        return {
            'updated': 'updated',
            'category': 'category',
            'length': 'word_length',
            'creator': 'user__username',
            'score': 'score',
            'default_key': 'score'
        }

class AnagramgameUpdateView(UpdateView):
    model = Anagramgame
    form_class = AnagramgamePlayForm
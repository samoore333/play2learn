from django.urls import path

from .views import (
    AnagramgameCreateView, AnagramgameDetailView, AnagramgameListView,
     AnagramgameUpdateView, score
)

app_name = 'anagram'
urlpatterns = [
    path('anagram/<slug>/play/', AnagramgameUpdateView.as_view(), name='play'),
    path('anagram/start/', AnagramgameCreateView.as_view(), name='start'),
    path('anagram/<slug>/', AnagramgameDetailView.as_view(), name='detail'),
    path('anagram/<slug>/score/', score, name='ajax-score'),
    path('', AnagramgameListView.as_view(), name='leaders'),
    path('creator/<username>/', AnagramgameListView.as_view(), name='creator'),
]
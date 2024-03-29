from django.urls import path

from .views import (
    MathgameCreateView, MathgameDetailView, MathgameListView,
     MathgameUpdateView, score
)

app_name = 'mathgame'
urlpatterns = [
    path('mathgame/<slug>/play/', MathgameUpdateView.as_view(), name='play'),
    path('mathgame/start/', MathgameCreateView.as_view(), name='start'),
    path('mathgame/<slug>/', MathgameDetailView.as_view(), name='detail'),
    path('mathgame/<slug>/score/', score, name='ajax-score'),
    path('', MathgameListView.as_view(), name='leaders'),
    path('creator/<username>/', MathgameListView.as_view(), name='creator'),
]

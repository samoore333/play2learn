from django.urls import path

from .views import (
    MathgameCreateView, MathgameDetailView, MathgameListView,
     MathgameUpdateView, playerScore
)

app_name = 'mathgame'
urlpatterns = [
    path('mathgame/<slug>/play/', MathgameUpdateView.as_view(), name='play'),
    path('mathgame/start/', MathgameCreateView.as_view(), name='start'),
    path('mathgame/<slug>/score/', playerScore, name='ajax-score'),
    path('mathgame/<slug>/', MathgameDetailView.as_view(), name='detail'),
    path('', MathgameListView.as_view(), name='leaders'),
]

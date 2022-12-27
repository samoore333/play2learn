from django.urls import path
from .views import (
    MathgameListView, MathgamePlayView, MathgameScoreView, MathgameStartView
)

app_name = 'mathgame'
urlpatterns = [
    path('start/play', MathgamePlayView.as_view(), name='play'),
    path('score', MathgameScoreView.as_view(), name='score'),
    path('start', MathgameStartView.as_view(), name='start'),
    path('leaderboard', MathgameListView.as_view(), name='leaders'),   
]

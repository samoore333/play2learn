from django.urls import path
from .views import (
    MathgameListView, MathgamePlayView, MathgameScoreView, MathgameStartView, MathGameView
)

app_name = 'mathgame'
urlpatterns = [
    path('mathgame/<int:pk>/play/', MathgamePlayView.as_view(), name='play'),
    path('mathgame/score', MathgameScoreView.as_view(), name='score'),
    path('mathgame/start/', MathgameStartView.as_view(), name='start'),
    path('math-facts-practice/', MathGameView.as_view(), name='math-facts-practice'),
    path('', MathgameListView.as_view(), name='list'),   
]

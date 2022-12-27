from django.urls import path
from .views import (
    MathgameListView, MathgameStartView, MathgamePlayView
)

app_name = 'mathgame'
urlpatterns = [
    path('start', MathgameStartView.as_view(), name='start'),
    path('mathgame/<int:pk>/play/', MathgamePlayView.as_view(), name='play'),
    path('leaderboard', MathgameListView.as_view(), name='leaders'),   
]

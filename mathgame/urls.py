from django.urls import path

from .views import (
    MathgameListView, MathgameStartView
)

app_name = 'mathgame'
urlpatterns = [
    path('start', MathgameStartView.as_view(), name='start'),
    path('leaderboard', MathgameListView.as_view(), name='leaders'),   
]

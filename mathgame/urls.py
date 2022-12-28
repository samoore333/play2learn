from django.urls import path

from .views import (
    MathgameDetailView, MathgameListView, MathgameStartView
)

app_name = 'mathgame'
urlpatterns = [
    path('mathgame/<int:pk>/', MathgameDetailView.as_view(), name='detail'),
    path('leaderboard', MathgameListView.as_view(), name='leaders'),
    path('start', MathgameStartView.as_view(), name='start'),  
]

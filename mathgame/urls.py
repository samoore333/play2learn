from django.urls import path
from .views import (
    MathgameCreateView, MathgameListView, MathGameView, MathgameUpdateView
)

app_name = 'mathgame'
urlpatterns = [
    path('mathgame/<int:pk>/update/', MathgameUpdateView.as_view(), name='update'),
    path('mathgame/play/', MathgameCreateView.as_view(), name='play'),
    path('math-facts-practice/', MathGameView.as_view(), name='math-facts-practice'),
    path('', MathgameListView.as_view(), name='list'),   
]

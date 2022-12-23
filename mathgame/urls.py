from django.urls import path
from .views import MathgameListView, MathGameView

app_name = 'mathgame'
urlpatterns = [
    path('', MathgameListView.as_view(), name='list'),
    path('math-facts-practice/', MathGameView.as_view(), name='math-facts-practice'),
]

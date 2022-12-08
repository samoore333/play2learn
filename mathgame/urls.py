from django.urls import path
from .views import MathgameListView

app_name = 'mathgame'
urlpatterns = [
    path('', MathgameListView.as_view(), name='list'),
]

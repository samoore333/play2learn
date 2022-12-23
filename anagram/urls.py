from django.urls import path
from .views import AnagramHuntView, AnagramListView

app_name = 'anagram'
urlpatterns = [
    path('', AnagramListView.as_view(), name='list'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
]

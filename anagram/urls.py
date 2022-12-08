from django.urls import path
from .views import AnagramListView

app_name = 'anagram'
urlpatterns = [
    path('', AnagramListView.as_view(), name='list')
]

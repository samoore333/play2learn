from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anagram/', include('anagram.urls')),
    path('mathfacts/', include('mathfacts.urls')),
    path('', include('pages.urls')),
]

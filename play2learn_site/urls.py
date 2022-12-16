from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('anagram/', include('anagram.urls')),
    path('contactus/', include('contactus.urls')),
    path('mathgame/', include('mathgame.urls')),
    path('', include('pages.urls')),
    path('reviews/', include('reviews.urls')),
]

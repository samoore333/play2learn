from django.urls import path

from .views import ReviewsAppView, ReviewsAppThanksView

app_name = 'reviews'
urlpatterns = [
    path('reviews-app/', ReviewsAppView.as_view(), name='app'),
    path('reviews-app/thanks/', ReviewsAppThanksView.as_view(), name='thanks'),
]

from django.urls import path

from .views import ContactUsView, ContactUsThanksView

app_name = 'contactus'
urlpatterns = [
    path('contactus-app/', ContactUsView.as_view(), name='app'),
    path('contactus-app/thanks/', ContactUsThanksView.as_view(), name='thanks'),
]

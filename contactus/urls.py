from django.urls import path

from .views import ContactUsAppView, ContactUsThanksView

app_name = 'contactus'
urlpatterns = [
    path('contactus-app/', ContactUsAppView.as_view(), name='app'),
    path('contactus-app/thanks/', ContactUsThanksView.as_view(), name='thanks'),
]

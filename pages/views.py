from django.views.generic import TemplateView
from reviews.models import Review

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
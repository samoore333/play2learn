from django.views.generic import TemplateView
from django.shortcuts import render
from reviews.models import Review

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def appReviews(request):
        reviews = Review.objects.filter(approved=True)
        comment = reviews.filter('comment')
        first = reviews.filter('first_name')
        context = {
            'comment': comment,
            'first': first
        }
        return render(request, 'pages/home.html', context=context)


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
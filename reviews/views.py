from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ReviewsForm

class ReviewsAppView(FormView):
    template_name = 'reviews/reviews.html'
    form_class = ReviewsForm
    success_url = reverse_lazy('reviews:thanks')

class ReviewsAppThanksView(TemplateView):
    template_name = 'reviews/thanks.html'
from django import template
from reviews.models import Review

register = template.Library()

@register.simple_tag # Get approved reviews
def appReviews():
    reviews = Review.objects.filter(approved=True)
    return reviews
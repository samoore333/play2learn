import random
from django import template

register = template.Library()

@register.simple_tag # Random number generator
def randNum(start, stop):
    return random.randint(start, stop)

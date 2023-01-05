from django import template
from django.conf import settings
from django.db import models
from django.urls import reverse
import random

from common.utils.text import unique_slug

def random_nums(num1, num2):

    if ['operation'] == '+':
        num1 = random.randint(1, ['max_number'])
        num2 = random.randint(1, ['max_number'])
    elif ['operation'] == 'x':
        num1 = random.randint(1, ['max_number'])
        num2 = random.randint(1, ['max_number'])
    elif ['operation'] == '-':
        num1 = random.randint(1, ['max_number'])
        num2 = random.randint(1, ['max_number'])
        if num2 > num1:
            num2, num1 = num1, num2
    else:
        num2 = random.randint(1, ['max_number'])
        numx = random.randint(1, ['max_number'])
        num1 = num2 * numx
    return num1, num2
    
    
class Mathgame(models.Model):
    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    OPERATION_CHOICES = [
        (ADDITION, 'Addition'),
        (SUBTRACTION, 'Subtraction'),
        (MULTIPLICATION, 'Multiplication'),
        (DIVISION, 'Division'),
    ]
    category = models.CharField(max_length=50, default='Math Facts Practice')
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES,
        default=ADDITION)
    max_number = models.IntegerField(default=10)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
    )
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    num1 = models.IntegerField(blank=True, null=True, default=random_nums)
    num2 = models.IntegerField(blank=True, null=True, default=random_nums)
    correct_answer = models.IntegerField(blank=True, null=True)
    incorrect_answer = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)
    time_left = models.IntegerField(default=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

    @property
    def correct_answers(self):
        return self.mathgames.filter(score=1).count()
    
    @property
    def timer(self):
        return self.mathgames.filter(time_left=-1).count()

    def get_absolute_url(self):
        return reverse('mathgame:play', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.operation
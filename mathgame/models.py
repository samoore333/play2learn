from django.conf import settings
from django.db import models
from django.urls import reverse
import random

from common.utils.text import unique_slug


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
    answer = models.IntegerField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    time_left = models.IntegerField(default=30)
    score = models.IntegerField(default=0)

    @property
    def get_random_nums():
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

    def get_absolute_url(self):
        return reverse('mathgame:play', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.operation

class Game_num(models.Model):
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.IntegerField(blank=True, null=True)
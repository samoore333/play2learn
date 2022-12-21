from django.conf import settings
from django.db import models

from common.utils.text import unique_slug

class Mathgame(models.Model):
    ADDITION = '+'
    SUBTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    OPERATION_CHOICES = [
        (ADDITION, '+'),
        (SUBTRACTION, '-'),
        (MULTIPLICATION, 'x'),
        (DIVISION, '/'),
    ]
    score = models.IntegerField()
    max_number = models.IntegerField()
    operation = models.CharField(max_length=1, choices=OPERATION_CHOICES,
    default=ADDITION)
    end_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.score
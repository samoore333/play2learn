from django.conf import settings
from django.db import models

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
    operation = models.CharField(max_length=1, choices=OPERATION_CHOICES,
        default=ADDITION)
    max_number = models.IntegerField(default=10)
    answer = models.IntegerField(blank=True)
    end_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.score
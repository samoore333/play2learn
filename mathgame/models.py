from django.db import models

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

    def __str__(self):
        return self.score
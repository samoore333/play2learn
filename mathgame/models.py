from django.conf import settings
from django.db import models
from django.urls import reverse

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
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    answer = models.IntegerField(blank=True)
    end_time = models.DateTimeField(blank=True, auto_now_add=True)
    score = models.IntegerField(blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    def get_absolute_url(self):
        return reverse('jokes:detail', args=[str(self.pk)])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return self.operation, self.max_number, self.end_time, self.score
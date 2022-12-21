from django.conf import settings
from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug

class Anagramgame(models.Model):
    WORD_LENGTH_CHOICES = [
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    ]
    word_length = models.CharField(max_length=1, choices=WORD_LENGTH_CHOICES,
    default=5)
    score = models.IntegerField()
    end_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.score
from django.db import models

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

    def __str__(self):
        return self.score
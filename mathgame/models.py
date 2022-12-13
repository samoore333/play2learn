from django.db import models

class Mathgame(models.Model):
    score = models.IntegerField()
    max_number = models.IntegerField()
    operation = models.CharField(max_length=1)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.score, self.max_number, self.operation, self.end_time
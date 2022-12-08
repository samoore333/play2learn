from django.db import models

class MathScore(models.Model):
    score = models.IntegerField
    max_number = models.IntegerField
    operation = models.CharField
    end_time = models.DateTimeField

    def __str__(self):
        return self.score, self.max_number, self.operation, self.end_time
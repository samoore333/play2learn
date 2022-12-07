from django.db import models

class Review(models.Model):
    comment = models.TextField(max_length=200)

    def __str__(self):
        return self.comment

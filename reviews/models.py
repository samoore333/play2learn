from django.db import models

class Review(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.comment

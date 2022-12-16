from django.db import models

class Review(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.comment

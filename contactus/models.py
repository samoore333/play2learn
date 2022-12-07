from django.db import models

class Contact(models.Model):
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.message


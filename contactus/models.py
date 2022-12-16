from django.db import models

class Contact(models.Model):
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.message


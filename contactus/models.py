from django.db import models

class Contact(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.message


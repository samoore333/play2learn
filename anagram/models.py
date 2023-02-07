from django.conf import settings
from django.db import models
from django.urls import reverse

from common.utils.text import unique_slug

class Anagramgame(models.Model):
    WORDLENGTH_CHOICES = [
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    ]
    category = models.CharField(max_length=50, default='Anagram Hunt')
    word_length = models.CharField(max_length=3, choices=WORDLENGTH_CHOICES, default='5')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('anagram:play', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)
    
    def __int__(self):
        return self.word_length

    def __int__(self):
        return self.score
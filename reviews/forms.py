from django.forms import ModelForm
from django import forms

from .models import Review

class ReviewsForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'email', 'comment']
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'message': forms.Textarea(
                attrs={'cols': 75, 'rows': 5}
            )
        }

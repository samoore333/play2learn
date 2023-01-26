from django.forms import ModelForm
from django import forms

from .models import Contact

class ContactUsForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'subject': forms.TextInput(),
            'message': forms.Textarea(
                attrs={'cols': 75, 'rows': 5}
            )
        }
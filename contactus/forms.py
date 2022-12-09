from django import forms

class ContactUsForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(max_length=200, required=True)
from django import forms

class ContactUsForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '75', 'rows': '5'})
    )
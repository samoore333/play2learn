from django import forms
from django.forms import NumberInput, ModelForm, Select

from .models import Anagramgame

class AnagramgameForm(ModelForm):
    class Meta:
        model = Anagramgame
        fields = ['word_length']
        widgets = {
            'word_length': Select(
                attrs={'autofocus': True, 
                    'choices': [(5, 5), (6, 6), 
                        (7, 7), (8, 8)]}
            )
        }
        help_texts = {
            'word_length': 'Enter a word length between 5 and 8.',
        }

class AnagramgamePlayForm(ModelForm):
    class Meta:
        model = Anagramgame
        fields = []
   
from django import forms
from django.forms import NumberInput, ModelForm, Select

from .models import Mathgame

class MathgameForm(ModelForm):
    class Meta:
        model = Mathgame
        fields = ['operation', 'max_number']
        widgets = {
            'operation': Select(
                attrs={'autofocus': True, 
                    'choices': [('+', 'Addition'), ('-', 'Subtraction'), 
                        ('*', 'Multiplcation'), ('/', 'Division')]}
            ),
            'max_number': NumberInput(
                attrs={'min': 1, 'max': 100}
            )
        }
        help_texts = {
            'operation': 'Select operation.',
            'max_number': 'Enter max number between 1 and 100.',
        }

class MathgamePlayForm(ModelForm):
    class Meta:
        model = Mathgame
        fields = ['score']
        widgets = {
            'score': NumberInput()
        }


   
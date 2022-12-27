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
            )
        }
        help_texts = {
            'operation': 'Select operation.',
            'max_number': 'Indicate maximum number.'
        }

class MathgamePlay(ModelForm):
    class Meta:
        model = Mathgame
        fields = ['answer']
        widgets = {
            'answer': NumberInput(
                attrs={'autofocus': True}
            )
        }
        help_texts = {
            'answer': 'Type your answer.'
        }

class MathgameScore(ModelForm):
    class Meta:
        model = Mathgame
        fields = ['score']
from django.forms import ModelForm 
from .models import Jogo

class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields['tipo', 'horário']
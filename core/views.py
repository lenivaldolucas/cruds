from django.shortcuts import render
from .models import Jogo
from .models import Jogadores
def listar_jogos(request):
    jogos = Jogo.objects.all()
    contexto = {
        'todos_jogos': jogos
    }
    return render(request, 'jogos.html', contexto)
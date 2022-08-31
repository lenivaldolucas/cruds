from django.shortcuts import render
from .models import Jogo
from .forms import JogoForm 
from .models import Jogadores
def listar_jogos(request):
    jogos = Jogo.objects.all()
    contexto = {
        'todos_jogos': jogos
    }
    return render(request, 'jogos.html', contexto)

def cadastrar_jogos(request):
    form = JogoForm(request.POST or None ) 

    contexto = {
        'form_jogo': form
    }
    return render(request, 'cadastrar_jogos.html', contexto)

def editar_jogos(request, id)
    jogo = Jogo.objects.get(pk=id)
    form = JogoForm(request.POST or None, instance=jogo)
    if form.is_valid():
        form.save()
        return redirect('todos_jogos')
    
    contexto = {
        'form_jogo': form 
    }
    return render(request, 'cadastrar_jogos.html', contexto)

def remover_jogos(request, id):
    jogo = Jogo.objects.get(pk=id)
    jogo.delete()
    return redirect('todos_jogos')
from django.shortcuts import render, redirect
from jogoMemoria.models import Jogador

#def define uma função
#sintaxe def nomedafunção(o oque ela vai fazer):
#return render(request,"nome do template que ele vai retornar")

def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def TelaInicial(request):
    jogadores = Jogador.objects.all()
    jogadores_lista = []
    for jogador in jogadores:
        jogadores_lista.append({
            'nome': jogador.nome,
            'tempo':jogador.tempo,
            'jogadas':jogador.jogadas
        })
    return render(request,'TelaInicial.html',{'itens':jogadores_lista})

def save(request):
    if request.POST:
        dados=request.POST
        jogador = Jogador(nome=dados.get("nome"),tempo=dados.get("tempo"),jogadas=dados.get("jogadas"))
        jogador.save()
        return redirect(TelaInicial)
# Create your views here.

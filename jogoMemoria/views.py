from django.shortcuts import render, redirect
from jogoMemoria.models import Jogador
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#def define uma função
#sintaxe def nomedafunção(o oque ela vai fazer):
#return render(request,"nome do template que ele vai retornar")

def login(request):
    return render(request,'login.html')

def usuario_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Usuário ou senha inválidas'})

    # jogo_listar = listar_jogos() # função para pegar a tabela e listar
    return render(request, 'registro/login.html')#, {'jogo_listar': jogo_listar})

@login_required
def index(request):
    return render(request,'index.html')

@login_required
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

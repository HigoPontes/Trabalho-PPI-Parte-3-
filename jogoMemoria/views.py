from django.shortcuts import render, redirect
from jogoMemoria.models import Jogador, Jogo
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

#def define uma função
#sintaxe def nomedafunção(o oque ela vai fazer):
#return render(request,"nome do template que ele vai retornar")

def format_time(seconds):
    try:
        seconds = int(seconds)  # Converte para inteiro, se possível
    except ValueError:
        return "0m 00s"  # Caso o valor não seja um número válido

    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}m {remaining_seconds:02d}s"

def listar_jogos():
    jogos = Jogo.objects.all().order_by('jogadas', 'tempo')
    jogo_listar = []
    posicao = 1
    for jogo in jogos:
        local_time = jogo.data_hora
        jogo.tempo = format_time(jogo.tempo)
        jogo_listar.append({
            "Posição": f"{posicao}°",
            "Nome": jogo.nome,
            "jogadas": jogo.jogadas,
            "Tempo": jogo.tempo,
            "Hora": local_time.strftime("%H:%M:%S"),
        })
        posicao += 1
    return jogo_listar


from django.http import JsonResponse

def login(request):
    return render(request,'login.html')

def usuario_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                jogador=user.jogador
            except Jogador.DoesNotExist:
                return render(request, 'registration/login.html', {'error': 'Jogador não encontrado'})
            
            login(request, user)
            # nome_usuario = user.get_full_name()
            # jogador = Jogador(nome=nome_usuario, tempo='0', jogadas='0')
            # jogador.save()
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Usuário ou senha inválidas'})

    # return render(request, 'registro/login.html')#, {'jogo_listar': jogo_listar})

    jogo_listar = listar_jogos()
    return render(request, 'registration/login.html', {'jogo_listar': jogo_listar})        

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

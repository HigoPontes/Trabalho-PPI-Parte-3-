# urls.py: usamos essa parte para criar as URL(link) entre as paginas 

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jogoMemoria.views import index, TelaInicial,save #Lembrar de adicionar uma virgula
# E importante colocar o nome da pagina a qual vc desse adicionar a url no import do jogoMemoria.views

urlpatterns = [
    #Aqui estão as url e a sua sintaxe
    #'nome do path',template que vai utilizar, name="Apelido que vai usar para chamar o path"
    path('',index,name="index"),
    path('TelaInicial/',TelaInicial,name="TelaInicial"),
    path('save',save,name='save')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

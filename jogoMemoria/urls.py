# urls.py: usamos essa parte para criar as URL(link) entre as paginas 
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jogoMemoria.views import index, TelaInicial,save, usuario_login #Lembrar de adicionar uma virgula
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('', usuario_login, name="login"),
    path('index/',index,name="index"),
    path('telaInicial/',TelaInicial,name="TelaInicial"),
    path('save',save,name='save'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

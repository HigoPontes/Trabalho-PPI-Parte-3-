from django.db import models
from django.contrib.auth.models import User
#Aqui eu estou definindo o modelo da lista do banco de dados. 
#Neste caso o Jogador que vai ter o seu nome, o tempo e as jogadas
class Jogador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nickname

class Jogo(models.Model):
    nome=models.CharField(
        max_length=100,null=False
    )
    tempo=models.CharField(
        max_length=20, null=False
    )
    jogadas=models.CharField(
        max_length=20,null=False
    )
    def __str__(self):
        return self.nome

# Create your models here.

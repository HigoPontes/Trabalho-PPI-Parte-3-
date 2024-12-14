from django.db import models
#Aqui eu estou definindo o modelo da lista do banco de dados. 
#Neste caso o Jogador que vai ter o seu nome, o tempo e as jogadas
class Jogador(models.Model):
    nome=models.CharField(
        max_length=100,null=False
    )
    tempo=models.CharField(
        max_length=20, null=False
    )
    jogadas=models.CharField(
        max_length=20,null=False
    )

#    def_str_(self):
#       return f"Jogador [nome={self.nome}]"

# Create your models here.

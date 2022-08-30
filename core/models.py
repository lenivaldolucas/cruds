from django.db import models

class Jogo(models.Model):
    tipo = models.CharField('tipo', max_length=100)
    horário = models.DateTimeField('hora')


class Jogadores(models.Model):
    nome = models.CharField('nome', max_length=100)
    posição = models.CharField('posição', max_length=100)



# Create your models here.

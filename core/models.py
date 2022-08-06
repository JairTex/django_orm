from django.contrib.auth import get_user_model
from django.db import models


class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Informe 16 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'
    
    def __str__(self):
        return self.numero

class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'
    
    def __str__(self):
        return self.nome

def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] # (object, boolean)

class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE) # 1 to 1
    montadora = models.ForeignKey('Montadora', on_delete=models.SET(set_default_montadora)) # 1 to m
    motoristas = models.ManyToManyField(get_user_model()) # N to M
    modelo = models.CharField('Modelo', max_length=30, help_text='Informe o modelo do Carro')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, help_text='Informe o preço do carro')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return f'{self.montadora} {self.modelo}'
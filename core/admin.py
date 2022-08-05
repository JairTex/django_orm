from django.contrib import admin

from .models import Carro, Chassi, Montadora


@admin.register(Chassi)
class ChassAdmin(admin.ModelAdmin):
    list_display = ('numero',)

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco')

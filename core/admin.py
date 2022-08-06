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
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    def get_motoristas(self, obj):
        return ', '.join([m.username for m in obj.motoristas.all()])
        #objects.get or objects.filter
        #Estudar List Comprehension
    
    get_motoristas.short_description = 'Motoristas'
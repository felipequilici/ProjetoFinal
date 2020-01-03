from django.contrib import admin
from .models import (
    marca,
    veiculo,
    pessoa,
    parametro,
    movimento_rotativo,
    mensalista,
    MovimentosMensalista
)

class movrotativoadmin(admin.ModelAdmin):
    list_display = ('veiculo','entrada', 'saida',  'valor_hora', 'total_horas', 'total', 'pago')

class movmensalistaadmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dataPagamento', 'total')



admin.site.register(pessoa)
admin.site.register(marca)
admin.site.register(veiculo)
admin.site.register(parametro)
admin.site.register(mensalista)
admin.site.register(MovimentosMensalista, movmensalistaadmin)
admin.site.register(movimento_rotativo, movrotativoadmin)

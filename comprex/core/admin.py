from django.contrib import admin
from comprex.core.models import Categoria, Produto

admin.site.register(Categoria)

#Personalização da tela de admin no DB
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'quantidade', 'preco', 'categoria_id')


admin.site.register(Produto, ProdutoModelAdmin)
from django.contrib import admin
from .models import Crianca

@admin.register(Crianca)
class CriancaAdmin(admin.ModelAdmin):
    # Definimos quais colunas aparecerão na lista geral
    # 'idade' é a propriedade que criamos no models.py anteriormente
    list_display = ('nome_completo', 'idade', 'data_nascimento', 'nome_responsavel', 'telefone')
    
    # Adiciona uma barra de pesquisa por nome da criança ou do responsável
    search_fields = ('nome_completo', 'nome_responsavel')
    
    # Adiciona filtros laterais (ajuda a agrupar por data de cadastro ou nascimento)
    list_filter = ('data_nascimento', 'data_cadastro')

    # Melhora a organização visual dentro do formulário de edição
    fieldsets = (
        ('Dados da Criança', {
            'fields': ('nome_completo', 'data_nascimento', 'foto')
        }),
        ('Informações de Contato', {
            'fields': ('nome_responsavel', 'telefone', 'telefone_alternativo')
        }),
    )
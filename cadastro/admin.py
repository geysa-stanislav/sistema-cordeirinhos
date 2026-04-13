from django.contrib import admin
from django.contrib.admin.models import LogEntry
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

# --- NOVA PARTE: Configuração do Histórico de Ações (Auditoria) ---
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # O que vai aparecer na tabela de listagem do painel
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message')
    
    # Filtros laterais úteis para encontrar o que alguém fez em um dia específico ou por usuário
    list_filter = ('action_time', 'user', 'action_flag')
    
    # Pesquisa para achar alterações em registros específicos
    search_fields = ('object_repr', 'change_message')
    
    # Travas de segurança: O Histórico é apenas leitura (não pode criar, editar ou excluir)
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
from django import forms
from .models import Crianca

class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = ['nome_responsavel', 'telefone', 'telefone_alternativo', 'nome_completo', 'data_nascimento', 'foto']
        
        widgets = {
            'nome_responsavel': forms.TextInput(attrs={'class': 'input-infantil', 'placeholder': 'Nome completo do responsável'}),
            'telefone': forms.TextInput(attrs={'class': 'input-infantil', 'placeholder': '(XX) 9XXXX-XXXX (WhatsApp Principal)'}),
            'telefone_alternativo': forms.TextInput(attrs={'class': 'input-infantil', 'placeholder': '(XX) 9XXXX-XXXX (WhatsApp Alternativo)'}),
            'nome_completo': forms.TextInput(attrs={'class': 'input-infantil', 'placeholder': 'Nome completo da criança'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'input-infantil', 'type': 'date'}),
            'foto': forms.FileInput(attrs={'class': 'input-infantil', 'accept': 'image/*'}),
        }
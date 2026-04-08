from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CriancaForm

def cadastro_view(request):
    # Se o usuário clicou no botão de enviar o formulário
    if request.method == 'POST':
        # request.FILES é obrigatório para capturar a foto 3x4 enviada
        form = CriancaForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save() # Salva direto no banco de dados
            messages.success(request, 'Cadastro da criança realizado com sucesso!')
            return redirect('cadastro') # Recarrega a página limpa para o próximo cadastro
    
    # Se o usuário apenas acessou o site pelo link
    else:
        form = CriancaForm()
    
    # Renderiza o HTML passando o formulário para a tela
    return render(request, 'cadastro/cadastro.html', {'form': form})
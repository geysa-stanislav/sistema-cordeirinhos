from django.db import models
from PIL import Image
from datetime import date # <-- Importação necessária para calcular a idade

class Crianca(models.Model):
    # Dados da Criança
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo da Criança")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    foto = models.ImageField(upload_to='fotos_3x4/', verbose_name="Foto 3x4")
    
    # Dados do Responsável
    nome_responsavel = models.CharField(max_length=200, verbose_name="Nome Completo do Responsável")
    telefone = models.CharField(max_length=20, verbose_name="Telefone Principal (WhatsApp)")
    telefone_alternativo = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone Alternativo (WhatsApp)")
    
    # Controle de sistema
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Criança"
        verbose_name_plural = "Crianças"

    def __str__(self):
        # Agora o nome aparece com a idade calculada ao lado
        return f"{self.nome_completo} ({self.idade} anos) - Resp: {self.nome_responsavel}"

    # <-- NOVA PROPRIEDADE: CALCULA A IDADE AUTOMATICAMENTE -->
    @property
    def idade(self):
        hoje = date.today()
        # Cálculo exato considerando se a criança já fez aniversário este ano
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade

    # Manutenção da sua função de redimensionamento
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 800 or img.width > 600:
                output_size = (600, 800)
                img.thumbnail(output_size)
                img.save(self.foto.path, optimize=True, quality=70)
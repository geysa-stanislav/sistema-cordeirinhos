from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cadastro.views import cadastro_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # Deixei a rota vazia ('') para ser a página inicial do site
    path('', cadastro_view, name='cadastro'), 
]

# Configuração essencial: avisa o Django como exibir as fotos 3x4 enquanto estamos programando
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls.py (config/urls.py)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import RegistroView  # Importa apenas RegistroView, já que ConfirmEmailView parece ausente

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a administração do Django
    path('', include('app.urls')),    # Inclui as URLs do aplicativo "app"
    path('cadastro/', RegistroView.as_view(), name='cadastro'),  # Rota para registro
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuração para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

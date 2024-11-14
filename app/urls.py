from django.urls import path
from django.contrib import admin
from app.views import IndexView, PragaView, NoticiaView, RegistroView, login_view, FerrugemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('praga/', PragaView.as_view(), name='praga'),
    path('noticia/', NoticiaView.as_view(), name='noticia'),
    path('cadastro/', RegistroView.as_view(), name='cadastro'),  # URL para registro
    path('login/', login_view, name='login'),  # URL para login
    path('ferrugem/', FerrugemView.as_view(), name='ferrugem'),  # URL para ferrugem
]

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from app.models import Noticia, Comentario
from app.forms import ComentarioForm, CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RegistroView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'cadastro.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático após o registro
            return redirect('index')  # Redireciona para a página inicial
        return render(request, 'cadastro.html', {'form': form})  # Exibe formulário com erros

def login_view(request):
    if request.method == "POST":
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=nome, password=senha)
        
        if user:
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return redirect('login')  # Redireciona para a página de login
    return render(request, 'login.html')

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class FerrugemView(View):
    def get(self, request):
        return render(request, 'ferrugem.html')

class PragaView(View):
    def get(self, request):
        return render(request, 'praga.html')

@method_decorator(login_required, name='dispatch')  # Exige login para visualizar e comentar
class NoticiaView(View):
    def get(self, request):
        noticias = Noticia.objects.all()
        comentario_form = ComentarioForm()
        return render(request, 'noticia.html', {
            'noticias': noticias,
            'comentario_form': comentario_form
        })

    def post(self, request):
        comentario_form = ComentarioForm(request.POST)
        noticia_id = request.POST.get('noticia_id')

        if comentario_form.is_valid() and noticia_id:
            noticia = get_object_or_404(Noticia, id=noticia_id)
            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.noticia = noticia
            novo_comentario.usuario = request.user  # Associa ao usuário logado
            novo_comentario.save()
            messages.success(request, 'Comentário adicionado com sucesso!')
            return redirect('noticia')  # Verifique se a URL 'noticia' está configurada corretamente

        # Exibe notícias com mensagem de erro
        noticias = Noticia.objects.all()
        messages.error(request, 'Erro ao comentar. Verifique os dados.')
        return render(request, 'noticia.html', {
            'noticias': noticias,
            'comentario_form': comentario_form,
        })
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
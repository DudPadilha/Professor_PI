from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    sobre = models.TextField()
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    link = models.URLField(max_length=200, null=True)
    # Outros campos da notícia

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="comentario_set")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

# models.py



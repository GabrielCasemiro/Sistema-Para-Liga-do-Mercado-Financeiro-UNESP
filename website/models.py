# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models
from utils import strip_accents
# Create your models here.


class Banner(models.Model):
    titulo = models.CharField(max_length=200, default="Título")
    descricao = models.CharField(max_length=200, default="Descrição")
    imagem = models.ImageField(null=True, blank=True, upload_to="banners/",default="#")
    
    def __str__(self):
        return strip_accents(self.titulo)
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(null=True, blank=True, upload_to="postagem/",default="#")
    descricao =  models.CharField(max_length=200, default="Descrição")
    conteudo = RichTextField()
    data = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User)
    TIPO_POST = (
        ('Artigos', 'Artigos'),
        ('Destaques da Semana', 'Destaques da Semana'),
        ('Editorial', 'Editorial'),
        ('Cursos', 'Cursos'),
        ('Eventos', 'Eventos')
    )
    tipo_post = models.CharField(max_length=25, choices=TIPO_POST)
    def __str__(self):
        return strip_accents(self.titulo) + ' - ' + strip_accents(self.tipo_post)

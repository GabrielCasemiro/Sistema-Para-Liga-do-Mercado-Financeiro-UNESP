# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import re
import unicodedata

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

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
    conteudo = RichTextUploadingField(config_name='default')
    data = models.DateTimeField(auto_now_add=False)
    #author = models.ForeignKey(User)
    TIPO_POST = (
        ('Artigos', 'Artigos'),
        ('Destaques da Semana', 'Destaques da Semana'),
        ('Editorial', 'Editorial'),
        ('Cursos e Eventos', 'Cursos e Eventos')
    )
    tipo_post = models.CharField(max_length=25, choices=TIPO_POST)
    def __str__(self):
        return strip_accents(self.titulo)
    
class Membro(models.Model):
    nome = models.CharField(max_length=100,default="nome")
    imagem = models.ImageField(null=True, blank=True, upload_to="membros/",default="#")
    cargo = models.CharField(max_length=150,blank=True)
    descricao =  models.TextField(max_length=600, default="Descrição")
    facebook = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    linkedin = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return strip_accents(self.nome)
    
class Foto(models.Model):
    imagem = models.ImageField(null=True, blank=True, upload_to="membros/", default="#")
    descricao =  models.CharField(max_length=100, default="Descricao")
    TIPO_POST = (
        ('Eventos', 'Eventos'),
        ('Cursos', 'Cursos')
    )
    categoria =  models.CharField(max_length=25, choices=TIPO_POST,default="Eventos")
    def __str__(self):
        return strip_accents(self.descricao)

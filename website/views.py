# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q
from utils import strip_accents
from .models import Banner, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    #BANNERS
    primeiro_banner = None
    banners = None
    banners_query = Banner.objects.all()
    if banners_query:
        primeiro_banner = banners_query[0]
        banners = banners_query[1:]
    #EDITORIAIS
    editoriais = Post.objects.filter(tipo_post="Editorial").order_by('data')[:3]
    #Cursos
    cursos = Post.objects.filter(tipo_post="Cursos").order_by('data')[:3]
    #Artigos
    artigos = Post.objects.filter(tipo_post="Artigos").order_by('data')[:3]
    #Destaque da Semana
    destaques = Post.objects.filter(tipo_post="Destaques da Semana").order_by('data')[:2]
    #EVENTOS
    eventos = Post.objects.filter(tipo_post="Eventos").order_by('data')[:3]
    #Post_popular
    post_popular = Post.objects.all().order_by('data')[:8]
    return render(request, 'index.html',{'primeiro_banner':primeiro_banner,'banners':banners,'editoriais': editoriais,'cursos':cursos,'artigos':artigos,'destaques':destaques,'eventos':eventos,'post_popular':post_popular})
#CATEGORIAS
def categoria_editorial(request):
    posts = Post.objects.filter(tipo_post='Editorial').order_by('data')
    titulo = "Editorial"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    #import pdb; pdb.set_trace()
    try:
        postagens = paginator.page(page)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)

    return render(request, 'category.html',{'posts':postagens,'titulo':titulo})

def categoria_artigos(request):
    posts = Post.objects.filter(tipo_post='Artigos').order_by('data')
    titulo = "Artigos"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    #import pdb; pdb.set_trace()
    try:
        postagens = paginator.page(page)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'posts':postagens,'titulo':titulo})

def categoria_destaques(request):
    posts = Post.objects.filter(tipo_post='Destaques da Semana').order_by('data')
    titulo = "Destaques da Semana"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    #import pdb; pdb.set_trace()
    try:
        postagens = paginator.page(page)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'posts':postagens,'titulo':titulo})

def categoria_cursos(request):
    posts = Post.objects.filter(tipo_post='Cursos').order_by('data')
    titulo = "Cursos"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    #import pdb; pdb.set_trace()
    try:
        postagens = paginator.page(page)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'posts':postagens,'titulo':titulo})
def categoria_eventos(request):
    posts = Post.objects.filter(tipo_post='Eventos').order_by('data')
    titulo = "Eventos"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    #import pdb; pdb.set_trace()
    try:
        postagens = paginator.page(page)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'posts':postagens,'titulo':titulo})
#PESQUISA
def pesquisa(request):
    tipo_categoria = request.POST.get('tipo_categoria','Editorial')
    texto_pesquisa = request.POST.get('texto_pesquisa','')
    posts = Post.objects.filter(Q(tipo_post=tipo_categoria, titulo__icontains=strip_accents(texto_pesquisa))|Q(tipo_post=tipo_categoria, descricao__icontains=strip_accents(texto_pesquisa))).order_by('data')
    
    page = request.GET.get('page', 10)
    paginator = Paginator(posts, 10)
    #import pdb; pdb.set_trace()
    try:
        postagens = paginator.page(page)
    except PageNotAnInteger:
        postagens = paginator.page(1)
    except EmptyPage:
        postagens = paginator.page(paginator.num_pages)
    return render(request, 'category.html',{'posts':postagens,'titulo':tipo_categoria,'texto_pesquisa':texto_pesquisa})


def galeria(request):
    return render(request, 'galery.html')


def page(request, num="1"):
    try:
        post = Post.objects.filter(id=num)
    except:
        pass
    return render(request, 'post-page.html',{'post':post[0]})

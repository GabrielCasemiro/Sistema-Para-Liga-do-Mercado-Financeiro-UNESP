"""lmf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^categoria_editorial', views.categoria_editorial, name='editorial'),
    url(r'^categoria_artigos', views.categoria_artigos, name='artigo'),
    url(r'^categoria_destaques', views.categoria_destaques, name='destaque'),
    url(r'^categoria_cursos', views.categoria_cursos, name='curso'),
    url(r'^categoria_eventos', views.categoria_eventos, name='eventos'),
    url(r'^page/(?P<num>[0-9]+)/$', views.page),
    url(r'^pesquisa', views.pesquisa, name='pesquisa'),
    url(r'^index', views.index, name='index'),
]
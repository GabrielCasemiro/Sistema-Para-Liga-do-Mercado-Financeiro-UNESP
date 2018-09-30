# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Banner, Post, Membro, Foto
# Register your models here.

admin.site.register(Banner)
admin.site.register(Post)
admin.site.register(Membro)
admin.site.register(Foto)
# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_by', 'created_at')
    list_filter = ('created_by', 'created_at')
    date_hierarchy = 'created_at'
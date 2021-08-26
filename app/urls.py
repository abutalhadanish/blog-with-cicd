# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # path("", include("authentication.urls")), # Auth routes - login / register
    path('accounts/', include('allauth.urls')),
    path("", include("app.urls"))             # UI Kits Html files
]

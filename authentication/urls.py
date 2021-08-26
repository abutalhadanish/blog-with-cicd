# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/'    , login_view,           name="login"   ),
    path('register/' , register_user,        name="register"),
    path("logout/"   , LogoutView.as_view(), name="logout"  )
]

# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('create/', views.create_blog, name='create_blog'),
    path('post/<int:pk>/', views.SinglePostView.as_view(), name='single_post'),
    path('', views.HomeView.as_view(), name='create_blog'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('index', views.index, name='index'),
    path('delete-post', views.delete_post, name='delete'),
    # path()

    # Matches any html file
    re_path(r'^index/.*\.*', views.pages, name='pages'),

]

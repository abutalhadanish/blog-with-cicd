# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    created_at= models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('single_post', kwargs={'pk':self.pk})
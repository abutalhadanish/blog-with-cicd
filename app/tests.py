# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.test import TestCase
from core.models import User
from app.models import Blog
from django.urls import reverse

def create_blog(text, user, **kwargs):
    return Blog.objects.create(text=text, created_by=user, **kwargs)

class UserModalTests(TestCase):
    
    def test_number_of_blogs(self):
        user = User.objects.create(username='test', email='test@example.com', password='test')
        Blog.objects.create(text='test1', created_by=user)
        Blog.objects.create(text='test2', created_by=user)
        self.assertEqual(user.number_of_blogs, 2)

class BlogViewTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='test', email='test@example.com', password='test')

    def test_valid_blog(self):
        
        self.client.login(username='test', password='test')
        blog = create_blog('test', self.user1)
        response = self.client.get(reverse('single_post', args=[blog.pk]))
        self.assertEqual(response.status_code, 200)

    def test_deleted_blog(self):
        # user = User.objects.create(username='test', email='test@example.com', password='test')
        # self.client.login(username='test', password='test')
        blog = create_blog('test', self.user1, is_active=False)
        response = self.client.get(reverse('single_post', args=[blog.pk]))
        self.assertEqual(response.status_code, 404)

    def test_valid_blog_on_homepage(self):
        # user = User.objects.create(username='test', email='test@example.com', password='test')
        # self.client.login(username='test', password='test')
        blog = create_blog('test 334455666', self.user1, is_active=True)
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'test 334455666')

    def test_deleted_blog_on_homepage(self):
        # user = User.objects.create(username='test', email='test@example.com', password='test')
        # self.client.login(username='test', password='test')
        blog = create_blog('test 334455666', self.user1, is_active=False)
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'test 334455666')


# Logged in should access the profile, rest shouldn't
# tests for various URLs

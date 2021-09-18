# -*- encoding: utf-8 -*-
"""
Simple Blogging System with CI/CD Demo - Made by Abutalha Danish
"""

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.urls.base import reverse
from .models import Blog
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import get_object_or_404


@login_required
def create_blog(request):
    # Handling both get and Post request for blog creation
    template_name = 'pages/create-blog.html'
    error_message = None
    if request.method == 'POST':
        text = request.POST.get('text')
        user = request.user

        if text == '':
            error_message = "You must input a blog content !"
            
        if not error_message:

            try:
                blog = Blog.objects.create(created_by=user, text=text)
            except Exception as e:
                error_message = str(e)

        print("POSt", text, error_message)
        if not error_message:
            return HttpResponseRedirect(reverse('home'))
    return render(request, template_name, {'error_message': error_message})

# @method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        return {'blogs': Blog.objects.filter(is_active=True).order_by('-created_at')}

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        return {'blogs': Blog.objects.filter(is_active=True, created_by=self.request.user).order_by('-created_at'), 'header': 'Blogs Created By Me', 'display_num_blogs': True}

# @method_decorator(login_required, name='dispatch')
class SinglePostView(TemplateView):
    template_name = 'pages/single.html'
    
    def get_context_data(self, **kwargs):
        # print("KW", kwargs)
        z = 1/0
        blog = get_object_or_404(Blog, is_active=True, pk=kwargs['pk'])
        return {'blog': blog}
    
@login_required
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required
def delete_post(request):
    blog_id = request.POST['post_id']
    try:
        blog = Blog.objects.get(pk=blog_id)
        if not request.user == blog.created_by:
            raise Exception('You do not have permission to delete this post.')

        blog.is_active = False
        blog.save()
        print("BBBB ", blog_id, blog)
        messages.success(request, 'Post successfully deleted.')
        return HttpResponseRedirect(reverse('home'))
    except:
        messages.error(request, 'Unable to delete post !')


    print("varss ", blog_id)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except Exception as e:
        print (e)
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

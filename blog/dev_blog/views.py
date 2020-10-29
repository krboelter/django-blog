from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class BlogView(TemplateView):
    template_name = 'dev_blog/blog.html'

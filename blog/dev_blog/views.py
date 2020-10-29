from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Entry

class BlogView(TemplateView):
    template_name = 'dev_blog/blog.html'

    def get(self, request):
        entry_list = Entry.objects.order_by('created_on')[:5]
        context = {
            'entries': entry_list
        }
        return render(request, self.template_name, context)

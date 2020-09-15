from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib import messages




class TestPage(TemplateView):
    template_name= 'test.html'

class ThanksPage(TemplateView):
    template_name='thanks.html'

class HomePage(TemplateView):
    template_name= 'index.html'
    def post(self, request, *args, **kwargs):
        lis=request.POST.getlist('favorite_pet')
        print(lis)
        if len(lis)>2:
            messages.warning(self.request,'Not more than two')
            return redirect('/')
        else:
            return redirect('/posts/')

from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


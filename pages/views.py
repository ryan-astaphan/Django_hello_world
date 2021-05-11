from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('<h1>Hello, World!</h1> <p>This is my first Django installation and app ever. I had previously learned a bit of Flask, which has made the introduction to Django an easy one.</p>')
    

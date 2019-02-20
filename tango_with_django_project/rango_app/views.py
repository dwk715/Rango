from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world !<br/> <a href='/rango/about'>See about</a>")

def about(request):
    return HttpResponse("about page. <br/> <a href='/rango/'>Return index</a>")
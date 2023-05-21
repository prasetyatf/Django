from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> Ini Index</h2>")

def about(request):
    return render(request, 'about.html')
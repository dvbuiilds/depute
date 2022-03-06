from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseServerError


def index(request):
    return render(request, 'index.html')

def outsource(request):
    return render(request, 'outsource.html')

def hiring(request):
    return render(request, 'hire.html')

def about(request):
    return render(request, 'about.html')
# Create your views here.

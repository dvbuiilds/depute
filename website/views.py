from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseServerError


def index(request):
    return render(request, 'index.html')
# Create your views here.

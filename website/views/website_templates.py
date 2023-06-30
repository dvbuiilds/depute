from django.shortcuts import render
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'index_new.html')

class About(View):
    def get(self, request):
        return render(request, 'about_new.html')

class Hire(View):
    def get(self, request):
        return render(request, 'hire.html')

class Outsource(View):
    def get(self, request):
        return render(request, 'outsource.html')

from django.shortcuts import render
from django.views import View

class Outsource(View):
    def get(self, request):
        return render(request, 'outsource.html')
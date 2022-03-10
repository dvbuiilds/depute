from django.shortcuts import render
from django.views import View

class Hire(View):
    def get(self, request):
        return render(request, 'hire.html')
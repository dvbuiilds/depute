from django.views import View
from django.shortcuts import render


class dashboard_cand(View):
    def get(self, request):
        return render(request, 'dashboard_cand.html')
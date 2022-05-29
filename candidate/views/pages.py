from django.views import View
from django.shortcuts import render


class dashboard_cand(View):
    def get(self, request):
        return render(request, 'dashboard_cand.html')

class candidate_details(View):
    def get(self, request):
        return render(request, 'cand_details.html')
    def post(self, request):
        print()
        return render(request, 'cand_details.html')
from django.views import View
from django.shortcuts import render


class dashboard_rec(View):
    def get(self, request):
        # Checking if the password submitted on the login form is accessible on other pages or not. But the result is No! The Password is not available on other pages.
        #print(request.POST.get('password'))
        return render (request, 'dashboard_rec.html')

class dashboard_cand(View):
    def get(self, request):
        return render(request, 'dashboard_cand.html')
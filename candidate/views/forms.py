from django.shortcuts import render, redirect
from django.views import View
from ..models import candidate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect


class multiStepForms1(View):
    def get(self, request):
        return redirect('can_details1.html')

    def post(self, request):
        print(request.POST)
        return redirect('cand_details2.html')

class multiStepForms2(View):
    def get(self, request):
        return redirect('can_details2.html')

    def post(self, request):
        print(request.POST)
        return redirect('cand_details3.html')

class multiStepForms3(View):
    def get(self, request):
        return redirect('can_details3.html')

    def post(self, request):
        print(request.POST)
        return redirect('cand_details4.html')

class multiStepFormsSubmission(View):
    def get(self, request):
        return redirect('can_details4.html')

    def post(self, request):
        print(request.POST)
        return redirect('dashboard_cand.html')
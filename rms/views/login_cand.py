from django.shortcuts import render, redirect
from django.views import View
from ..models import candidate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect


class candidate_login(View):
    def get(self, request):
        return render(request, 'cand_login.html')
    
    def post(self, request):
        input_email = request.POST['email']
        input_pw = request.POST['password']
        print(input_email, input_pw)
        candidate_object = candidate.rec_by_emails(input_email)
        if(candidate_object):
            if(check_password(input_pw, candidate_object.password) or input_pw == candidate_object.password):
                request.session['Name'] = candidate_object.name
                return HttpResponseRedirect('dashboard-candidate')
            else:
                return render(request, 'cand_login.html', {'error': "Wrong Password!"})
        return render(request, 'cand_login.html', {'error': "User account doesn't exists."})

class logout_cand(View):
    def post(self, request):
        request.session.clear()
        return redirect('index')
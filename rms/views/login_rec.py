from django.shortcuts import render, redirect
from django.views import View
from ..models import recruiter
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect


class recruiter_login(View):
    def get(self, request):
        return render(request, 'rec_login.html')
    
    def post(self, request):
        input_email = request.POST['email']
        input_pw = request.POST['password']
        print(input_email, input_pw)
        recruiter_object = recruiter.rec_by_emails(input_email)
        if(recruiter_object):
            if(check_password(input_pw, recruiter_object.password) or input_pw == recruiter_object.password):
                request.session['Name'] = recruiter_object.name
                return HttpResponseRedirect('dashboard-recruiter')
            else:
                return render(request, 'rec_login.html', {'error': "Wrong Password!"})
        return render(request, 'rec_login.html', {'error': "User account doesn't exists."})

class logout_recruit(View):
    def post(self, request):
        request.session.clear()
        return redirect('index')
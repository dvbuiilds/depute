from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from ..models import candidate
from curses.ascii import isalpha


class cand_create_account(View):
    message = {
        'error': None
    }
    userrec = candidate()

    def get(self, request):
        return render(request, 'cand_account.html')
    
    def post(self, request):
        input_fname = request.POST['fname']
        input_lname = request.POST['lname']
        input_number = request.POST['number']
        input_email = request.POST['email']
        input_pw1 = request.POST['password1']
        input_pw2 = request.POST['password2']
        #print(input_fname, input_lname, input_number, input_email, input_pw1)
        if(input_fname.isalpha() and input_lname.isalpha()):
            print('All Alphas')
        else:
            self.message['error'] = 'Name should contain alphabets only. '

        self.message['error'] = (self.message['error'] if self.message['error'] else '') + ('' if input_number[0]=='+' else ' Number should start with Country Code (Ex. +91)')
        
        # Checking if password matches or not.
        if(input_pw1 != input_pw2):
            self.message['error'] = self.message['error'] + ' Passwords are not matching!'
        
        if(self.message['error']):
            return render(request, 'cand_account.html', self.message)
        else:
            if(candidate.cand_by_emails(input_email)):
                self.message['error'] = (self.message['error'] if self.message['error'] else '') + ' Email already exists. Consider Signing in or use another email.'
                return render(request, 'cand_account.html', self.message)
            
            self.userrec.name = input_fname.upper() + ' ' + input_lname.upper()
            self.userrec.email = input_email
            self.userrec.phno = input_number
            self.userrec.password = make_password(input_pw1)
            self.userrec.filled = False
            self.userrec.save()
            # Session object is to be made.
            return render(request, 'cand_login.html')
        return redirect('/create-account-candidate')
        
    
    def check_name(self, name):
        for c in name:
            if(isalpha(c) or c==' '):
                pass
            else:
                return False
        return True
    
    def check_number(self, number):
        if(number[0]!='+'):
            return 'Number should start with +(91) Country Code. '
        return ''
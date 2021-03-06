from django.views import View
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from ..models import recruiter
from curses.ascii import isalpha


class rec_create_account(View):
    message = {
        'error': None
    }
    userrec = recruiter()

    def get(self, request):
        return render(request, 'rec_account.html')
    
    def post(self, request):
        # Importing the fields from the POST form.
        input_fname = request.POST['fname']
        input_lname = request.POST['lname']
        input_co_name = request.POST['company']
        input_number = request.POST['number']
        input_email = request.POST['email']
        input_pw = request.POST['password']

        # Printing whatever is imported! Password is to be removed in the later phase.
        #print(input_fname, input_lname, input_co_name, input_number, input_email, input_pw)

        # Validation of the user input.
        if(input_fname.isalpha() and input_lname.isalpha()):
            print('All Alphas')
        else:
            self.message['error'] = 'Name should contain alphabets only. '

        self.message['error'] = (self.message['error'] if self.message['error'] else '') + ('' if input_number[0]=='+' else ' Number should start with Country Code (Ex. +91)')

        if(self.message['error']):
            return render(request, 'rec_account.html', self.message)
        else:
            # If user already exists.
            if(recruiter.rec_by_emails(input_email)):
                self.message['error'] = (self.message['error'] if self.message['error'] else '') + ' Email already exists. Consider Signing in or use another email.'
                return render(request, 'rec_account.html', self.message)
            
            # Otherwise we save it as a user.
            self.userrec.name = input_fname.upper() + ' ' + input_lname.upper()
            self.userrec.company_name = input_co_name
            self.userrec.email = input_email
            self.userrec.phno = input_number
            self.userrec.password = make_password(input_pw)
            self.userrec.save()

            # Session object is to be made.
            return render(request, 'rec_login.html')
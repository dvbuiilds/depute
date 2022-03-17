from django.shortcuts import render
from django.views import View
from ..models import recruiter, application
from django.contrib.auth.hashers import check_password

class recruiter_main(View):
    def generate_csv(self, request):
        recruiter_id = request.session['rec_id']
        
        # the dashboard page will be sending us the job id.
        job_id = 1
        applicationset = application.get_apps_by_job_id(job_id)
        print(applicationset)
        

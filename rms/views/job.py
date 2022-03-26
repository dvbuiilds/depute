from django.views import View
from django.shortcuts import redirect, render
from ..models.jobs import jobs
from ..models.application import application
from ..models.candidate import candidate
from datetime import datetime
import csv
from django.http import HttpResponse


class post_job(View):
    job_obj = jobs()
    rec = None
    jid = None

    def post(self, request):
        self.rec = request.session['recruiter']
        self.jid = request.session['job_id']
        self.job_obj.company_name = request.POST['company']
        self.job_obj.cat1 = request.POST['cat1']
        self.job_obj.cat2 = request.POST['cat2']
        self.job_obj.description = request.POST['company']
        self.job_obj.experience = request.POST['company']
        self.job_obj.vacancies = request.POST['company']
        self.job_obj.location = request.POST['company']
        self.job_obj.last_date = request.POST['company']
        self.job_obj.post_date = datetime.today() # Maybe needs to be chanegd.
        self.job_obj.is_active = True
        self.job_obj.rec_id = request.POST['recruiter']
        self.job_obj.role_name = request.POST['role']

        self.job_obj.save()
        return redirect('')

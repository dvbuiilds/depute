from django.db import models
from .category1 import category_a
import csv
from django.http import HttpResponse

class candidate(models.Model):
    cid = models.BigAutoField(primary_key=True, null=False)
    cname = models.CharField(max_length=30)
    cage = models.IntegerField()
    cemail = models.EmailField()
    cpassword = models.CharField(max_length=30)
    job_cat = models.ForeignKey(to=category_a, on_delete=models.SET_NULL, default=1, null=True)
    cphno = models.CharField(max_length=20)
    resume_link = models.FileField(upload_to='rms/resumes/')
    
    @staticmethod
    def get_cand_by_id(_id):
        return  candidate.objects.filter(cid = _id)
    
    @staticmethod
    def get_all_cands(request):
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Name', 'Age', 'Email', 'Phone'])
        for cand in candidate.objects.all():
            writer.writerow([cand.cname, cand.cage, cand.cemail, cand.cphno])

        response['Content-Disposition'] = "attachment; filename=allcandidateslist.csv"
        return response
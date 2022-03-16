from xml.etree.ElementInclude import default_loader
from django.db import models
from .category1 import category_a

class candidate(models.Model):
    cid = models.BigAutoField(primary_key=True, null=False)
    cname = models.CharField(max_length=30)
    cage = models.IntegerField()
    cemail = models.EmailField()
    cpassword = models.CharField(max_length=30)
    job_cat = models.ForeignKey(to=category_a, on_delete=models.SET_NULL, default=1, null=True)
    cphno = models.CharField(max_length=10)
    resume_link = models.FileField(upload_to='rms/resumes/')
    
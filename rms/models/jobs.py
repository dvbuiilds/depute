from asyncio.windows_events import NULL
from django.db import models
from .recruiter import recruiter
from .category1 import category_a
from .category2 import category_b

class jobs(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    rec_id = models.ForeignKey(to=recruiter, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=100)
    cat1 = models.ForeignKey(to=category_a, to_field='cta_id', null=True, on_delete=models.SET_NULL, default=1)
    cat2 = models.ForeignKey(to=category_b, to_field='ctb_id', null=True, on_delete=models.SET_NULL, default=1)
    description = models.TextField(max_length=1500, default='')
    stipend = models.FloatField()
    location = models.CharField(max_length=50)
    vacancies = models.IntegerField()
    company_name = models.CharField(max_length=30)
    experience = models.BooleanField(default=1)
    post_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__ (self):
        return self.job_id
    
    @staticmethod
    def get_jobs_by_rec_id(_id):
        return jobs.objects.filter(rec_id = _id)
    
    @staticmethod
    def get_active_jobs():
        return jobs.objects.filter(is_active = True)
from django.db import models

class recruiter(models.Model):
    rid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phno = models.CharField(max_length=10)
    company_name = models.CharField(max_length=30)


from django.db import models

class recruiter(models.Model):
    rid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    phno = models.CharField(max_length=20)
    company_name = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def register(self):
        self.save()
    
    @staticmethod
    def rec_by_emails( _email):
        try:
            return recruiter.objects.get(email = _email)
        except:
            return False


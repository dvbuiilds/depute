from django.db import models


class candidate(models.Model):
    name = models.CharField(max_length=30, null=True)
    phno = models.CharField(max_length=20, null=True) # on form ask whatsapp number.
    email = models.EmailField(null=True)
    password = models.CharField(max_length=200, null=True)
    filled =  models.BooleanField(default=False)

    @staticmethod
    def cand_by_emails( _email):
        try:
            return candidate.objects.get(email = _email)
        except:
            return False
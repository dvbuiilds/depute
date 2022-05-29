from django.db import models


class candidate(models.Model):
    name = models.CharField(max_length=30, null=False)
    phno = models.CharField(max_length=20, null=False) # on form ask whatsapp number.
    email = models.EmailField(null=False)
    password = models.CharField(max_length=200, null=False)
    filled =  models.BooleanField(default=False)

    @staticmethod
    def cand_by_emails( _email):
        try:
            return candidate.objects.get(email = _email)
        except:
            return False
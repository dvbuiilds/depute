from django.db import models

class category_a(models.Model):
    cta_id = models.BigAutoField(primary_key=True)
    cta_name = models.CharField(max_length=20)
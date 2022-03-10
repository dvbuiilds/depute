from django.db import models

class category_b(models.Model):
    ctb_id = models.BigAutoField(primary_key=True)
    ctb_name = models.CharField(max_length=20)
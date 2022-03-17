from django.db import models
from ..models.category1 import category_a

class category_b(models.Model):
    ctb_id = models.BigAutoField(primary_key=True)
    major_cat = models.ForeignKey(to=category_a, default=1, on_delete=models.SET_DEFAULT)
    ctb_name = models.CharField(max_length=20)
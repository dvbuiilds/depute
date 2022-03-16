from os import stat
from django.db import models
from .recruiter import recruiter
from .candidate import candidate


class application(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    rec_id = models.ForeignKey(to=recruiter, on_delete=models.CASCADE, default=1)
    can_id = models.ForeignKey(to=candidate, on_delete=models.CASCADE, default=1)
    app_time = models.DateTimeField()
    
    def __str__(self):
        return self.app_id
    
    @staticmethod
    def get_apps_by_cid(cid):
        return application.objects.filter(can_id = cid)
    
    @staticmethod
    def get_apps_by_rec_id(rid):
        return application.objects.filter(rec_id = rid)
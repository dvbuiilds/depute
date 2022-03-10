from django.db import models
from .recruiter import recruiter
from .candidate import candidate


class application(models.Model):
    app_id = models.BigAutoField(primary_key=True)
    rec_id = models.ForeignKey(to=recruiter, on_delete=models.CASCADE, default=1)
    can_id = models.ForeignKey(to=candidate, on_delete=models.CASCADE, default=1)
    app_time = models.DateTimeField()

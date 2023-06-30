from django.db import models
from candidate.models.user import candidate

class canddetails(models.Model):
    cand = models.ForeignKey(to=candidate, on_delete=models.CASCADE, default=1)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, null=True, default="Others")

    # Education.
    qualification = models.CharField(max_length=20, null=True)
    specialization = models.CharField(max_length=30, null=True)
    university = models.CharField(max_length=200, null=True)
    course_type = models.CharField(max_length=30, null=True)
    pass_year = models.CharField(max_length=4, null=True)
    skills = models.CharField(max_length=300, null=True)

    # Employment Details
    work_status = models.CharField(max_length=20, null=True)
    experience = models.FloatField()
    emp_status = models.BooleanField(default=False)
    recent_comp = models.CharField(max_length=100, null=True)
    job_title = models.CharField(max_length=100, null=True)
    curr_city = models.CharField(max_length=100, null=True)
    working_since = models.IntegerField()
    curr_ctc = models.FloatField()
    curr_fix_ctc = models.FloatField()
    notice_period = models.CharField(max_length=10, null=True)
    notice_nego = models.BooleanField()
    industry = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=20, null=True)

    # Future employment details
    exp_ctc = models.FloatField()
    pref_job_type = models.CharField(max_length=15, null=True)
    pref_emp_type = models.CharField(max_length=15, null=True)
    pref_work_loc = models.CharField(max_length=30, null=True)
    pref_work_ind = models.CharField(max_length=100, null=True)
    pref_work_dept = models.CharField(max_length=100, null=True)

    # Final
    relocate = models.BooleanField()
    send_updates = models.BooleanField() # for emails and whatsapp.
    resume_link = models.URLField()
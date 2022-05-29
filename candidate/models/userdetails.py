from django.db import models
from candidate.models.user import candidate

class canddetails(models.Model):
    cand = models.ForeignKey(to=candidate, on_delete=models.CASCADE, default=1)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, null=False, default="Others")

    # Education.
    qualification = models.CharField(max_length=20, null=False)
    specialization = models.CharField(max_length=30, null=False)
    university = models.CharField(max_length=200, null=False)
    course_type = models.CharField(max_length=30, null=False)
    pass_year = models.CharField(max_length=4, null=False)
    skills = models.CharField(max_length=300, null=False)

    # Employment Details
    work_status = models.CharField(max_length=20, null=False)
    experience = models.FloatField()
    emp_status = models.BooleanField(default=False)
    recent_comp = models.CharField(max_length=100, null=False)
    job_title = models.CharField(max_length=100, null=False)
    curr_city = models.CharField(max_length=100, null=False)
    working_since = models.IntegerField()
    curr_ctc = models.FloatField()
    curr_fix_ctc = models.FloatField()
    notice_period = models.CharField(max_length=10, null=False)
    notice_nego = models.BooleanField()
    industry = models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=100, null=False)
    job_type = models.CharField(max_length=20, null=False)

    # Future employment details
    exp_ctc = models.FloatField()
    pref_job_type = models.CharField(max_length=15, null=False)
    pref_emp_type = models.CharField(max_length=15, null=False)
    pref_work_loc = models.CharField(max_length=30, null=False)
    pref_work_ind = models.CharField(max_length=100, null=False)
    pref_work_dept = models.CharField(max_length=100, null=False)

    # Final
    relocate = models.BooleanField()
    send_updates = models.BooleanField() # for emails and whatsapp.
    resume_link = models.URLField()
from django.contrib import admin
from .models import candidate, recruiter, jobs, application, category_a, category_b

# Register your models here.
admin.site.register(candidate)
admin.site.register(recruiter)
admin.site.register(jobs)
admin.site.register(application)
admin.site.register(category_a)
admin.site.register(category_b)
from django.contrib import admin
#from .models import candidate, recruiter, jobs, application, category_a, category_b
import csv
from django.http import HttpResponse


# class CandidateAdmin(admin.ModelAdmin):
#     list_display=('cname', 'cphno', 'cemail')
#     def download_csv(self, request, queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)

#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])

#         return response
#     download_csv.short_description = "Export CSV"
#     actions = [download_csv]


# # Register your models here.
# admin.site.register(candidate, CandidateAdmin)
# admin.site.register(candidate)
# admin.site.register(recruiter)
# admin.site.register(jobs)
# admin.site.register(application)
# admin.site.register(category_a)
# admin.site.register(category_b)
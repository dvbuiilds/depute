from django.shortcuts import redirect, render
#from rms.models.application import application
from candidate.models import candidate
import csv
from django.http import HttpResponse


# def cand_apps_by_jid(request):
#     jid=1
#     response = HttpResponse(content_type='text/csv')
#     writer = csv.writer(response)
#     writer.writerow(['Name', 'Age', 'Email', 'Phone'])
#     for app in application.get_apps_by_job_id(jid):
#         #print(app.app_id, app.can_id_id, app.job_id)
#         cand = candidate.objects.get(cid=app.can_id_id)
#         #writer.writerow([cand.cname, cand.cage, cand.cemail, cand.cphno])
#         writer.writerow([])

#     response['Content-Disposition'] = "attachment; filename=candidateslist.csv"
#     return response

from django.urls import path
from .views.acc_rec import *
from .views.login_rec import *
#from .views.get_apps import cand_apps_by_jid
from .views.pages import *
from .middlewares import Rauthmiddleware


urlpatterns = [
    path('login-recruiter',  recruiter_login.as_view(), name="recruit-login"),
    path('create-account-recruiter',  rec_create_account.as_view(), name="recruit-create-account"),
    path('logout', logout_recruit.as_view(), name='logout'),
    path('dashboard-recruiter', Rauthmiddleware(dashboard_rec.as_view()), name='dashboard-recruiter'),
#    path('download', Rauthmiddleware(cand_apps_by_jid), name='CSV'),
]
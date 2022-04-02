from django.urls import path
from .views.acc_rec import *
from .views.acc_cand import *
from .views.login_rec import *
from .views.login_cand import *
from .views.get_apps import cand_apps
from .views.pages import *
from .middlewares.auth import Rauthmiddleware, Cauthmiddleware


urlpatterns = [
    path('login-recruiter',  recruiter_login.as_view(), name="recruit-login"),
    path('login-candidate',  candidate_login.as_view(), name="candidate-login"),
    path('create-account-recruiter',  rec_create_account.as_view(), name="recruit-create-account"),
    path('create-account-candidate',  cand_create_account.as_view(), name="candidate-create-account"),
    path('logout', logout_recruit.as_view(), name='logout'),
    path('logout-user', logout_cand.as_view(), name='logout'),
    path('download', Rauthmiddleware(cand_apps), name='CSV'),
    path('dashboard-recruiter', Rauthmiddleware(dashboard_rec.as_view()), name='dashboard-recruiter'),
    path('dashboard-candidate', Cauthmiddleware(dashboard_cand.as_view()), name='dashboard-candidate'),
]
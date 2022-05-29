from django.urls import path
from .views.acc_cand import *
from .views.login_cand import *
from .middlewares import Cauthmiddleware
from .views.pages import *


urlpatterns = [
    path('login-candidate',  candidate_login.as_view(), name="candidate-login"),
    path('create-account-candidate',  cand_create_account.as_view(), name="candidate-create-account"),
    path('logout-user', logout_cand.as_view(), name='logout'),
    path('dashboard-candidate', Cauthmiddleware(dashboard_cand.as_view()), name='dashboard-candidate'),
]
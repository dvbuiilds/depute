from django.urls import path

from rms.views.rec_account import rec_create_account
from .views import *

urlpatterns = [
    path('recruit-login',  recruiter_login.as_view(), name="recruit-login"),
    path('rec-create-account',  rec_create_account.as_view(), name="recruit-create-account"),
]
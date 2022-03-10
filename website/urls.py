from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = "index"),
    path('about-us', About.as_view(), name = "about-us"),
    path('outsource-to-us', Outsource.as_view(), name="outsource-to-us"),
    path('hire-with-us', Hire.as_view(), name="hire-with-us"),
]
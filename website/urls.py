from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('about-us', views.about, name = "about-us"),
    path('outsource-to-us', views.outsource, name="outsource-to-us"),
    path('hire-with-us', views.hiring, name="hire-with-us"),
]
from django.contrib import admin
from .models.user import candidate
from .models.userdetails import canddetails

# Register your models here.
admin.site.register(candidate)
admin.site.register(canddetails)
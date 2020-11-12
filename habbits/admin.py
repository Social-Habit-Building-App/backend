from django.contrib import admin
from .models import Habbit

#
admin.site.register(Habbit)
admin.site.site_header = "social habit"

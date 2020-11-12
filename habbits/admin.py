from django.contrib import admin
from .models import habbit

#
admin.site.register(habbit)
admin.site.site_header = "social habit"

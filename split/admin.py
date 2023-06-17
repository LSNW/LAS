from django.contrib import admin
from .models import ServiceRecord
from .models import AVFile

admin.site.register(ServiceRecord)
admin.site.register(AVFile)
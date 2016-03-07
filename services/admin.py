from django.contrib import admin
from .models import *
from .forms import ServiceForm

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
	list_display = ["service_name","link","description"]
	list_filter = ["service_name"]
	list_editable = ["link"]
	form = ServiceForm

admin.site.register(Service, ServiceAdmin)

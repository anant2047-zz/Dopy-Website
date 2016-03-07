from django.contrib import admin
# from .forms import SignUpForm
from .models import HomePage

# Register your models here.
class HomePageAdmin(admin.ModelAdmin):
	list_display = ["__str__","sliderImages"]
	model = HomePage



admin.site.register(HomePage, HomePageAdmin)
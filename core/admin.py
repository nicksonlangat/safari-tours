from django.contrib import admin
from .models import County, Hotel,Attraction

# Register your models here.

admin.site.register(County)
admin.site.register(Hotel)
admin.site.register(Attraction)
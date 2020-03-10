from django.contrib import admin

# Register your models here.
from .models import ServisClient, Bike, Servis, Comments

admin.site.register(ServisClient)
admin.site.register(Servis)
admin.site.register(Bike)
admin.site.register(Comments)

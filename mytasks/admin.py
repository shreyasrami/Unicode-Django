from django.contrib import admin
from .models import Weather
# Register your models here.

admin.site.register(Weather)
admin.site.site_header = 'My administration'
admin.site.site_title = 'Weather'
admin.site.index_title = 'Site admin panel'
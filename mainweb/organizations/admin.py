from django.contrib import admin
from .models import Moim

class MoimAdmin(admin.ModelAdmin):
    list_display=['moim_name', 'created_date' ]
    search_fields=['moim_name']
    

admin.site.register(Moim, MoimAdmin)
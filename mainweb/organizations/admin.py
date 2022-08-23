from django.contrib import admin
from .models import Moim

class MoimAdmin(admin.ModelAdmin):
    list_display=['name', 'created_date' ]
    search_fields=['name']
    

admin.site.register(Moim, MoimAdmin)
from django.contrib import admin
from .models import Patient


class doctorview(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'date',
        'message'
    ]
    list_filter = ('date',)
    search_fields = ('name',)

admin.site.register(Patient,doctorview)

from django.contrib import admin

from .models import Report, Update


class ReportAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'id', 'file_name', 'city', 'state', 'region', 'last_update',
        'confirmed', 'deaths', 'recovered'
    ]
    search_fields = ('file_name', 'city', 'state', 'region')
    list_per_page = 1000


class UpdateAdmin(admin.ModelAdmin):
    list_display = ['id', 'started_at', 'ended_at', 'elapsed_time']

admin.site.register(Report, ReportAdmin)
admin.site.register(Update, UpdateAdmin)

from django.contrib import admin
from .models import ScrapeRequest

# Register your models here.


class ScrapeRequestAdmin(admin.ModelAdmin):
    fields = ('email', 'csv_path', 'result_csv_path', 'status', 'created_at')
    readonly_fields = ('created_at', 'status')
    list_display = ('email', 'csv_path', 'current_status', 'created_at')

    def current_status(self, obj):
        return obj.status == 0 and 'Pending' or 'Delivered'


admin.site.site_header = 'Administration'
admin.site.register(ScrapeRequest, ScrapeRequestAdmin)

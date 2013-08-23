from leaves.models import Leave
from django.contrib import admin

class LeaveAdmin(admin.ModelAdmin):
    fields = ["author", "start_date", "end_date"]
    list_display = ["author", "start_date", "end_date"]
    list_filter = ["author", "start_date", "end_date"]

admin.site.register(Leave, LeaveAdmin)

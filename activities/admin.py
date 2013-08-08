from activities.models import Author, Activity
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    pass

class ActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Activity, ActivityAdmin)

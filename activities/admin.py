from activities.models import Author, Activity, Category
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    fields = ["fullname", "email", "password", "onsite_team"]
    list_display = ["fullname", "email", "onsite_team"]

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details' ,  { 'fields' : ["author","ticket_number", "description"]}),
        ('Categorization', { 'fields' : ["activity_type", "hours_worked"]}),
        ('Date Information', { 'fields' : ["activity_date"]})
    ]
    list_display = ["activity_type","author", "activity_date"]
    list_filter = ["author", "activity_date"]

class CategoryAdmin(admin.ModelAdmin):
    fields = ["category_type", "parent_category"]
    list_display = ["category_type", "parent_category"]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Category, CategoryAdmin)

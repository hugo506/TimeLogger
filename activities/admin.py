from activities.models import AuthorInfo, Activity, Category
from django.contrib import admin

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details' ,  { 'fields' : ["author","ticket_number", "description"]}),
        ('Categorization', { 'fields' : ["activity_type", "hours_worked"]}),
        ('Date Information', { 'fields' : ["activity_date"]})
    ]
    list_display = ["activity_type","author", "activity_date"]
    list_filter = ["author", "activity_date"]

class CategoryAdmin(admin.ModelAdmin):
    fields = ["category_name", "parent_category", "category_description"]
    list_display = ["category_name", "parent_category"]


class AuthorInfoAdmin(admin.ModelAdmin):
    list_display = ["author", "designation", "onsite_team"]

admin.site.register(AuthorInfo, AuthorInfoAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Category, CategoryAdmin)

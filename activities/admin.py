from activities.models import Author, Activity, Category
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    fields = ["fullname", "email", "password", "onsite_team"]

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Details' ,  { 'fields' : ["author","ticket_number", "description"]}),
        ('Categorization', { 'fields' : ["activity_type", "hours_worked"]}),
        ('Date Information', { 'fields' : ["activity_date"]})
    ]


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 8

class CategoryAdmin(admin.ModelAdmin):
    fields = ["category_type", "parent_category"]
    inlines = [CategoryInline]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Category, CategoryAdmin)

from django.db import models
from django.utils import timezone # not used yet
from django.conf import settings

class AuthorInfo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    onsite_team = models.BooleanField() # True: onsite, False: Offshore
    designation = models.CharField(max_length=200)

    def __unicode__(self):
        return self.author.username

    class Meta:
        verbose_name_plural = "Author Information"

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    parent_category = models.CharField(max_length=200)
    category_description = models.TextField(default="NA")
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

class Activity(models.Model):
    description = models.TextField(help_text="Acitivity description")
    activity_type = models.ForeignKey(Category, blank=False)
    activity_date = models.DateField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False)
    ticket_number = models.IntegerField(default=0)
    hours_worked = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ["-activity_date"]
        verbose_name_plural = "Activities"

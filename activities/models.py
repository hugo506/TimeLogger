from django.db import models
from django.utils import timezone # not used yet

class Author(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    onsite_team = models.BooleanField() # True: onsite, False: Offshore
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.fullname

    def nickname(self):
        return self.fullname.split()[0]


class Category(models.Model):
    category_type = models.CharField(max_length=200)
    parent_category = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_type


class Activity(models.Model):
    description = models.TextField()
    activity_type = models.ForeignKey(Category)
    activity_date = models.DateField()
    author = models.ForeignKey(Author)
    ticket_number = models.IntegerField()
    hours_worked = models.IntegerField(default=0)
    categorization = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.description


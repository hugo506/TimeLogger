from django.db import models
from django.utils import timezone
from django.conf import settings

class Leave(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Leaves"

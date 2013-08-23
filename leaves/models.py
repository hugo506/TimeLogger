from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.exceptions import ValidationError

class Leave(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Leaves"

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date cannot be earlier than start date")

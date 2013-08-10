from django import forms
from activities.models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ('author', )

class ReportsDateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

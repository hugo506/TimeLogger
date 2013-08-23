from django import forms
from leaves.models import Leave

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        exclude = ('author', )

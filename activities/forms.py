from django import forms
from activities.models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ('author', )

class ReportsDateForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()

    def clean(self):
        cleaned_data = super(ReportsDateForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date > end_date:
            raise forms.ValidationError("Start date has to be earlier than end date!")


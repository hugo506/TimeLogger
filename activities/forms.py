from django import forms
from activities.models import Activity, Category
from django.forms.widgets import TextInput

class NumberInput(TextInput):
    input_type = 'number'


class ActivityForm(forms.ModelForm):
    description = forms.CharField(widget=forms.widgets.TextInput(attrs={
                                            'class':'form-control',
                                            "value": "NA",
                                            'placeholder': 'Ticket description'}))
    activity_date = forms.CharField(widget=forms.widgets.TextInput(attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Date of activity'}))
    ticket_number = forms.CharField(widget=NumberInput(attrs={
                                            'step': '1',
                                            'class': 'form-control',
                                            "value": 0,
                                            'placeholder': 'Ticket worked on'}))
    hours_worked = forms.CharField(widget=NumberInput(attrs={
                                            'step': '0.5',
                                            'class': 'form-control',
                                            'placeholder': 'e.g. 2 or 1.5'}))
    comment = forms.CharField(widget=forms.widgets.Textarea(attrs={
                                            'class': 'form-control', 'cols' : 40, 'rows': 3,
                                            'placeholder': 'Enter task description'}))

    def clean_hours_worked(self):
        MAX_HOURS = 4
        if float(self.cleaned_data["hours_worked"]) > MAX_HOURS:
            raise forms.ValidationError("You cant add more than %d hours on any task" % MAX_HOURS)
        return self.cleaned_data["hours_worked"]

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
            raise forms.ValidationError("End date cannot be earlier than start date")
        return cleaned_data

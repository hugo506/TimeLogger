from django import forms
from activities.models import Activity

class ActivityForm(forms.ModelForm):
    description = forms.CharField(widget=forms.widgets.Textarea(attrs={
                                            'class':'form-control', 'cols':40, 'rows': 3,
                                            'placeholder' : 'Autopopulated from redmine'}))
    activity_date = forms.CharField(widget=forms.widgets.TextInput(attrs={
                                            'class': 'form-control' }))
    ticket_number = forms.CharField(widget=forms.widgets.TextInput(attrs={
                                            'class': 'form-control' }))
    hours_worked = forms.CharField(widget=forms.widgets.TextInput(attrs={
                                            'class': 'form-control' }))
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


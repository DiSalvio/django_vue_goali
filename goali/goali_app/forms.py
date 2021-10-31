from django import forms
from .models import Goal


class GoalForm(forms.Form):
    name = forms.TextField()
    description = forms.TextField()
    status = forms.CharField(label="status",
            widget=forms.RadioSelect(choices=Goal.STATUS_CHOICES))

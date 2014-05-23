from django import forms
from django.utils import timezone
import datetime

class project_form(forms.Form):
    name = forms.CharField(max_length=100)
    start = forms.DateInput()
    description = forms.CharField(widget=forms.Textarea)

class task_form(forms.Form):
    name = forms.CharField(max_length=100)
    project_id=forms.CharField()
    start = forms.DateInput()
    description = forms.CharField(widget=forms.Textarea)
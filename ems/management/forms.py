from django import forms

class DepartmentForm(forms.Form):
    name = forms.CharField(max_length=256, required=True)
    location = forms.CharField(max_length=100, required=True)

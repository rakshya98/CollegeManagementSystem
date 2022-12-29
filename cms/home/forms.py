from dataclasses import field
import imp
from django.forms import ModelForm
from django import forms
from .models import   Employee
class EmployeeCreateForm(ModelForm):
    Emp_first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Employee
        fields = '__all__'
from django.forms import ModelForm
from django import forms
from .models import Organization, Student


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
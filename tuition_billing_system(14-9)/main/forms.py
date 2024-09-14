from django import forms
from .models import Branch, Student

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'email', 'phone', 'subjects_available', 'password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'parent_name', 'phone_number1', 'phone_number2', 'address', 'subjects']

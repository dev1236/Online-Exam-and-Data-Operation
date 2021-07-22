from django import forms
from .models import student_data as student

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model= student
        fields= ('st_name','mobile','college','branch','semester','photo','signature','usn')
    
from django import forms
from .models import Student

class StudentForm(forms.Form):
    name=forms.CharField(max_length=25)
    age=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea)


class StudentForm1(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={'address':forms.Textarea(),
                }
        labels={'name':'enter your name',}
        





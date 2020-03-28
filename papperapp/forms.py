from django import forms

class NameForm(forms.Form):
    student_name = forms.CharField(label='Student name', max_length=100)

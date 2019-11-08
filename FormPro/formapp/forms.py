from django import forms

class emform(forms.Form):
    name=forms.CharField(max_length=120)
    desig=forms.CharField(max_length=120)
    sal=forms.IntegerField()

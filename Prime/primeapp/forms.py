from django import forms

class pform(forms.Form):
    maxlimit=forms.IntegerField()
    minlimit=forms.IntegerField()

from django import forms

class pform(forms.Form):
    nam=forms.CharField(max_length=120)
    cat=forms.CharField(max_length=120)
    pri=forms.IntegerField()
    spe=forms.CharField(max_length=120)

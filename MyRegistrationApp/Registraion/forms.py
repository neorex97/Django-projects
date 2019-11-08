from django import forms

class Reg_frm(forms.Form):
    username=forms.CharField(max_length=120)
    email=forms.EmailField(max_length=150)
    phone=forms.CharField(max_length=12)
    pwd=forms.CharField(max_length=125)
    cpwd=forms.CharField(max_length=120)

class login_frm(forms.Form):
    username = forms.CharField(max_length=120)
    pwd = forms.CharField(max_length=120)




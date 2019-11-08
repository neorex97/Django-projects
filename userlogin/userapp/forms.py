from django import forms
from .models import user
#forms

class reg_frm(forms.Form):
    username = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=120)
    email = forms.EmailField(max_length=120)
    password = forms.CharField(max_length=120)
    cpwd = forms.CharField(max_length=120)

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("password")
        cpwd = cleaned_data.get("cpwd")
        if cpwd!= pwd:
            msg = "password mismatch"

            self.add_error('password',msg)
            self.add_error('cpwd', msg)
        name = cleaned_data.get("username")
        if user.objects.filter(username=name):
            mesg = "user already exists"
            self.add_error('username',mesg)

        pho = cleaned_data.get('phone')




class login_frm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)


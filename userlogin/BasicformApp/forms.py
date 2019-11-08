from BasicformApp.models import Usr
from django import forms


class new_frm(forms.ModelForm):
    class Meta():
        model = Usr
        # exclude=[]
        # field = ()
        fields = '__all__'

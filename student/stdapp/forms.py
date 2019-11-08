from stdapp.models import User

from django import forms


class std_frm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
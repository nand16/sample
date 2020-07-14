from app.models import user_info
from django import forms
from django.contrib.auth.models import User

class user_data_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')

class user_info_form(forms.ModelForm):
    class Meta:
        model = user_info
        fields = ('portflio','profile_pic')

from django import forms
from app.models import *
from django.contrib.auth.models import User

class User_Form(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','email','password']
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username':''} 

class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','profile_pic']

       



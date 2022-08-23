from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(required=False)
    description = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ['name', 'email', 'nickname', 'description',]
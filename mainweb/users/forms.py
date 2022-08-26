from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    password = None        
    name = forms.CharField(label='이름', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8',}), 
    )
    nickname = forms.CharField(label='닉네임', widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength':'8',}), 
    )           

    class Meta:
        model = get_user_model()
        fields = ['name', 'nickname',]
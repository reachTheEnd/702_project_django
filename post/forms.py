from django.contrib.auth.models import User
from django import forms
from .models import Employee

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 


class ProfileForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ['department', 'distance']

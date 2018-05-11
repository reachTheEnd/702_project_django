from django.contrib.auth.models import User
from django import forms
from .models import Employee
from django.contrib.auth import authenticate, login, logout, get_user_model


User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 


class ProfileForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ['department', 'distance']

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	# def clean(self, *args, **kwargs):
	# 	username = self.cleaned_data['username']
	# 	password= self.cleaned_data['password']
	# 	user = authenticate(username=username, password=password)
	# 	if not user:
	# 		raise forms.ValidationError('not exist')

	# 	if not user.check_password(password):
	# 		raise forms.ValidationError('incorrect password')


	# 	if not user.is_active:
	# 		raise forms.ValidationError('not active')

	# 	return super (UserLoginForm, self).clean(*args, **kwargs)

















from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import User, Employee
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from .forms import UserForm, ProfileForm, UserLoginForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
# class HomeView(TemplateView):
# 	template_name = 'post/base.html'

# 	def get_context_data(self):
# 	    context = super().get_context_data(request)
# 	    user = User
# 	    if user.is_active:
# 	    	print('hello world')
# 	    	print(user.pk)
# 	    	profile = Employee
# 	    	# b = Employee.objects.get(user = user.get_username(self))
# 	    	# print(b)
# 	    	print(request)
	
# 	    return context
def index(request):
	return render(request, 'post/base_not_log.html')


def logined(request):
	b = Employee.objects.get(user = request.user)
	print(b.department)
	print(b.distance)
	return render(request, 'post/base.html')


def logout_view(request):
	logout(request)
	return render(request, 'post/base_not_log.html')

class UerLoginForm(TemplateView):
	template_name = 'post/user_login.html'

	def get(self, request):
		form = UserLoginForm
		return render(request, self.template_name, {'form': form})
	def post(self, request):
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password= form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('post:logined')
				else:
					return render(request, self.template_name, {'form': form})
	    #             return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
	    #     else:
	    #         return render(request, 'music/login.html', {'error_message': 'Invalid login'})
	    # return render(request, 'music/login.html')

			return render(request, self.template_name, {'form': form})












class UserFormView(TemplateView):
	template_name = 'post/registration_form.html'	

	def get(self, request):
		form = UserForm()
		profile_form = ProfileForm()
		return render(request, self.template_name, {'form': form, 'profile_form': profile_form})

	def post(self, request):
		form = UserForm(request.POST)
		profile_form = ProfileForm(request.POST)

		if form.is_valid():

			user = form.save(commit = False)
			profile = profile_form.save(commit = False)
			username=form.cleaned_data['username']
			password= form.cleaned_data['password']

			department=profile_form.cleaned_data['department']
			distance=profile_form.cleaned_data['distance']
			user.set_password(password)

			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					profile.user = request.user
					profile.save()
					return redirect('post:logined') 

		return render(request, self.template_name, {'form': form, 'profile_form': profile_form})











 
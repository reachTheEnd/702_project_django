from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from .forms import UserForm, ProfileForm

# Create your views here.
def index(request):
	#return HttpResponse('hello world')
	return render(request, 'post/base.html')
 
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
					return redirect('post:index')


		return render(request, self.template_name, {'form': form, 'profile_form': profile_form})











 
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse,HttpResponse
# from users.serializers import RegisterSerializer
from django.contrib.auth.models import User, auth
from django.utils.decorators import method_decorator
from django.conf import settings



def register(request):

	if request.method == 'POST':
		# countrys = request.POST['country']
		# phones = request.POST['phone']

		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# instances = Userinfo.objects.create(user = instance, country=countrys, phone=phones)
			# instances.save()
			messages.success(request, f'Account created for you!')
			return redirect('/login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			p_form.save()
			u_form.save()
			messages.success(request, f'your account has been updated!')
			return redirect('/profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context={
		'u_form':u_form,
		'p_form':p_form,
	}
	return render(request, 'users/profile.html', context)

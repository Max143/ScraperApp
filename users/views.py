from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserProfileForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def Register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			form.save()
			messages.success(request, f'Your Account Has Been Created! You Can Able To Login.')
			return redirect('bloglist')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})




@login_required
def Profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = UserProfileForm(request.POST, instance=request.user.profile)
		if p_form.is_valid():
			job = p_form.cleaned_data['job']
			location = p_form.cleaned_data['location']
			p_form.save()
			messages.success(request, f'Your Profile Has Been Updated.')
			return redirect('profile')
	else:
		p_form = UserProfileForm()
	return render(request, 'users/profile.html', {'p_form':p_form})
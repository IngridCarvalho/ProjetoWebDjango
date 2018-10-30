from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from .forms import RegisterForm, EditAccountForm

def register(request):
	template_name = 'registration/register.html'

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.username, password = form.cleaned_data['password1'])
			login(request, user)
			return redirect('core:home')
	else:
		form = RegisterForm()

	context = {
		'form': form
	}

	return render(request, template_name, context)

def logout_view(request):
	logout(request)
	return redirect(settings.LOGIN_REDIRECT_URL)

@login_required
def dashboard(request):
	template_name = 'registration/dashboard.html'
	return render(request, template_name)

@login_required
def edit(request):
    template_name = 'registration/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

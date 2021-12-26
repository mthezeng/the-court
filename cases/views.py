from cases.forms import RegistrationForm, EditProfileForm
from cases.models import Case
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	featured_case_list = Case.objects.all()
	context = {'featured_case_list': featured_case_list}
	return render(request, 'cases/index.html', context)

def detail(request, case_id):
	try:
		case = Case.objects.get(pk=case_id)
		args = {'case': case}
	except Case.DoesNotExist:
		raise Http404('This case is not in the database.')
	return render(request, 'cases/detail.html', args)


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/cases')
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'cases/register.html', args)

@login_required
def view_profile(request):
	args = {'user': request.user}
	return render(request, 'cases/profile.html', args)

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/cases/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form, 'user': request.user}
		return render(request, 'cases/edit_profile.html', args)

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/cases/profile')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form, 'user': request.user}
		return render(request, 'cases/change_password.html', args)

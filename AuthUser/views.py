from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from AuthUser.forms import RegistrationForm, ProfileForm


# Create your views here.
def regitration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {"form": form})


@login_required
def userProfile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(to='profile')

    else:
        form = ProfileForm()

    return render(request, 'auth/profile.html', {"form": form})
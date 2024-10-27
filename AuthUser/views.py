from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from AuthUser.forms import RegistrationForm, ProfileForm, UpdatePasswordForm, EditUserInfoForm


# Create your views here.
#registro de usuarios
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

#perfil del usuario
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

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('profile')

@login_required
def changeUserInfo(request):
    if request.method == 'POST':
        form = EditUserInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditUserInfoForm(instance=request.user)

    return render(request, 'auth/EditUserInfo.html', {'form': form})
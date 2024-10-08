from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from auth.forms import RegistrationForm


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



def logoutview(request):
    logout(request)
    return redirect('login')
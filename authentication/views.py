from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from authentication.forms import LoginForm


# Create your views here.

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('customers')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})


def logout_page(request):
    logout(request)

    return render(request, 'authentication/logout.html')


def register(request):
    return render(request, 'authentication/register.html')

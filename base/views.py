from .forms import SignupForm, SigninForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def homepage(request):
    return render(request, 'homepage.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('signup')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        user = form.is_valid()
        if user:
            login(request, user)
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
    else:
        form = SigninForm()

    return render(request, 'signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='/signin')
def dashboard(request):
    return render(request, 'dashboard.html')

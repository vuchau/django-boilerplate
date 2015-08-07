from .forms import SignupForm, UserEditForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            return redirect('signin')
    else:
        form = SignupForm()

    base_template = 'layout_ajax.html' if request.is_ajax() else 'layout.html'
    ajax_header = 'Sign Up' if request.is_ajax() else ''
    return render(request, 'signup.html', {
        'form': form,
        'base_template': base_template,
        'ajax_header': ajax_header})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            login(request, user)
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
    else:
        form = AuthenticationForm()

    base_template = 'layout_ajax.html' if request.is_ajax() else 'layout.html'
    ajax_header = 'Sign In' if request.is_ajax() else ''
    return render(request, 'signin.html', {
        'form': form,
        'next': request.GET.get('next', 'dashboard'),
        'base_template': base_template,
        'ajax_header': ajax_header})


def signout(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='signin')
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid(request.user.id):
            user = User.objects.get(id=request.user.id)
            user.__dict__.update(**form.cleaned_data)
            user.save()
            return redirect('profile_edit')
    else:
        form = UserEditForm(request.user._wrapped.__dict__)

    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='signin')
def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            password = form.cleaned_data['new_password1']
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=user.username, password=password)
            login(request, auth_user)
            return redirect('profile_edit_password')
    else:
        form = PasswordChangeForm(user=request.user,)

    return render(request, 'edit_password.html', {'form': form})

from .forms import SignupForm, UserEditForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from profile.models import User
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            auth_user = authenticate(email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password'])
            login(request, auth_user)
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
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
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.__dict__.update(**form.cleaned_data)
            user.save()
            return redirect('dashboard')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

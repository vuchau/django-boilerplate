from .forms import SigninForm, SignupForm, ProfileEditForm, ForgotPasswordForm, ResetPasswordForm
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from general.tasks import email


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
        form = SigninForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            login(request, user)
            next_page = request.GET.get('next', 'dashboard')
            return redirect(next_page)
    else:
        form = SigninForm()

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


def reset_password(request, uid):
    show404 = False
    try:
        user = User.objects.get(uid=uid)
    except User.DoesNotExist:
        #   User doesn't exist
        show404 = True

    if not user.reset_password_requested:
        #   User has not requested a password reset
        show404 = True

    if show404:
        raise Http404("Password reset token doesn't exist")

    if request.method == 'POST':
        form = ResetPasswordForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            auth_user = authenticate(email=user.email,
                                     password=form.cleaned_data['new_password1'])
            login(request, auth_user)
            user.reset_password_requested = False
            user.save()
            return redirect('dashboard')
    else:
        form = ResetPasswordForm()

    return render(request, 'password_reset.html', {
        'form': form,
        'uid': uid
    })


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
                user.reset_password_requested = True
                user.save()
                reset_password_link = reverse('reset_password', kwargs={'uid': user.uid})
                absolute_link = request.build_absolute_uri(reset_password_link)
                email.delay(to=user.email, template="forgot_password", template_data={
                    "link": absolute_link
                })
            except User.DoesNotExist:
                pass
            return redirect('homepage')
    else:
        form = ForgotPasswordForm()

    base_template = 'layout_ajax.html' if request.is_ajax() else 'layout.html'
    ajax_header = 'Forgot Password' if request.is_ajax() else ''
    return render(request, 'password_forgot.html', {
        'form': form,
        'base_template': base_template,
        'ajax_header': ajax_header})


@login_required(login_url='signin')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['new_password1']:
                auth_user = authenticate(email=user.email,
                                         password=form.cleaned_data['new_password1'])
                login(request, auth_user)
            return redirect('dashboard')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

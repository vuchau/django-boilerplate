from .forms import SignupForm, SigninForm
from .tasks import add
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
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

    base_template = 'layout_ajax.html' if request.is_ajax() else 'layout.html'
    ajax_header = 'Sign Up' if request.is_ajax() else ''
    return render(request, 'signup.html', {
        'form': form,
        'base_template': base_template,
        'ajax_header': ajax_header})


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

    base_template = 'layout_ajax.html' if request.is_ajax() else 'layout.html'
    ajax_header = 'Sign In' if request.is_ajax() else ''
    return render(request, 'signin.html', {
        'form': form,
        'base_template': base_template,
        'ajax_header': ajax_header})


def signout(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='/signin')
def dashboard(request):
    return render(request, 'dashboard.html')


def test_celery(request):
    add.delay(1, 2)
    return HttpResponse("Celery task called")

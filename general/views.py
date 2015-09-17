from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def homepage(request):
    return render(request, 'homepage.html')


@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')


@api_view()
def rest(request):
    return Response({"message": "Hello, world!"})

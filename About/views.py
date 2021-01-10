from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home_view(request):
    return render(request, 'homepage.html')


def About_Us(request):
    return render(request, 'AboutUs.html')


def donate(request):
    return render(request, 'donate.html')

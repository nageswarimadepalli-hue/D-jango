from django.shortcuts import render

from django.http import HttpResponse

from .models import student
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")
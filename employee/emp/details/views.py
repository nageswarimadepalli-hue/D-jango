from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
   
def emp_details(request):
    return HttpResponse("Employee Details")
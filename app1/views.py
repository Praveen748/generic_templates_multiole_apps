from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_string1(request):
    return HttpResponse('<marquee>This is my first  app_string1')
def app_template(request):
    return render(request,'appf_irst.html')


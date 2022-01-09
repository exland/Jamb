from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testing(request):
    return HttpResponse('Hello world')

def homepage(request):
    return render(request, 'homepage.html')
   # return HttpResponse('Homepage')

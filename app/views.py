from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Anjali(request):
    return HttpResponse('<marquee><h1>This is my 4th project</h1></marquee>')

from django.http import HttpResponse
def Tulasi(request):
    return HttpResponse('<h2>This is my mother Name</h2>')

from django.http import HttpResponse
def Amrita(request):
    return HttpResponse('<marquee>Hii Amrita!! How Are You</marquee>')

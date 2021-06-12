from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is home')


def about(request):
    return HttpResponse('This is about')


def contact(request):
    return HttpResponse('This is contact')
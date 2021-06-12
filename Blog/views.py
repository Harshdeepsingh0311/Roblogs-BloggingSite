from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('This is blogHome')


def blogPost(request, slug):
    return HttpResponse(f'This is blogPost: {slug}')
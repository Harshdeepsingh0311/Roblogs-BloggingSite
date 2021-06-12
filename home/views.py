from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('desc')
        contact_post = Contact(name=name, email=email, phone=phone, content=content)
        contact_post.save()
        messages.success(request, 'Your Message Has Been Sent...')
    return render(request, 'home/contact.html')
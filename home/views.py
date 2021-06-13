from Blog.models import Post
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
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form correctly...")

        else:
            contact_post = Contact(name=name, email=email, phone=phone, content=content)
            contact_post.save()
            messages.success(request, 'Your Message Has Been Sent...')
    
    return render(request, 'home/contact.html')


def search(request):
    query=request.GET.get('query')
    if query!=None:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__contains=query)
        allPostsCategory = Post.objects.filter(category__contains=query)
        allPostsAuthor = Post.objects.filter(author__contains=query)
        allPostsSlug = Post.objects.filter(slug__contains=query)
        allPosts=allPostsTitle.union(allPostsSlug, allPostsAuthor, allPostsCategory, allPostsContent)
        
    else:
        messages.warning(request, 'No search results found. Please Refine Your Query.')
        return render(request, 'home/search.html')
    context = {'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', context)
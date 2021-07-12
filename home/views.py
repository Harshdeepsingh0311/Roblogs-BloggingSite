from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Contact
from Blog.models import Post

# HTML pages
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    messages.success(request, 'If you want your blog to be published in my website you can contact me through this form, and i will get back to you within a day...')
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


# Authentication APIs
def handleSignUp(request):
    if request.method == 'POST':
        # get the post parameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        print(username, fname, lname)

        # Checks for erroneous inputs
        if len(username)>50:
            messages.error(request, "Username must less than 50 characters.") 
            redirect('home')

        if not username.isalnum():
            messages.error(request, "Username can include only letters and numbers.") 
            redirect('home')

        if pass1!=pass2:
            messages.warning(request, "Your Passwords Do Not Match")
            redirect('home') 

        #Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, f"{fname} Your Roblogs Account has been created.") 
        return redirect('/')
    else:
        return HttpResponse('404 Not Found')


def handleLogin(request):
    if request.method == 'POST':
        loginUsername = request.POST.get('loginUsername')
        loginPassword = request.POST.get('loginpass')

        user = authenticate(username=loginUsername, password=loginPassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In...")
            return redirect('home')

        else:
            messages.error(request, "Invalid Credentials: Please Try Agian.")
            return redirect('home')
    return HttpResponse('404 Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
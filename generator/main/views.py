from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm, SavedForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, SavedName

# Create your views here.

def home(request):
    if request.method == 'POST':
        generated_name = request.POST.get('generated_name')
        request.session['generated_name'] = generated_name  # Store in session

    return render(request, 'main/home.html')

#displays all post objects' fields in the shape of cards
def feed(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id = post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'main/feed.html', {"posts": posts})


#requires user to be logged in, recieves the generated name selected when "post" button is pressed and sets default value of generated_name field to that name
@login_required(login_url = "/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect("/feed")
    else:
        generated_name = request.GET.get('generated_name', '')
        form = PostForm(initial = {'generated_name': generated_name})
    return render(request, 'main/create_post.html', {"form" : form})

@login_required(login_url = "/login")
def profile(request):
    return render(request, 'main/profile.html')

#saves data from reigster form in order to store newly created login credentials
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', {"form": form})
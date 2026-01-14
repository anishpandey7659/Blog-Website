from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Comment
from .form import PostForm,CommentForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.
# views.py

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # <--- request.FILES is required!
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_view')
    else:
        form = PostForm()
    return render(request, 'app1/post_create.html', {'form': form})

def home_view(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(category__name__icontains=search_query)
        ).order_by('-date')
    else:
        posts = Post.objects.all().order_by('-date')
    
    return render(request, 'app1/index.html', {'posts': posts})

def explore_more(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        # Search in BOTH title AND category
        posts = Post.objects.filter(
            Q(title__icontains=search_query) | Q(category__name__icontains=search_query)
        ).order_by('-date')
    else:
        # Show all posts if no search
        posts = Post.objects.all().order_by('-date')
    
    return render(request, 'app1/more.html', {'posts': posts})

def about(request):
    return render(request,'app1/about.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    
    return render(request, 'app1/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # optional: restrict editing to author only
    if post.author != request.user:
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'app1/post_edit.html', {
        'form': form,
        'post': post
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('home_view')

    return render(request, 'app1/post_delete.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatically log in after registration
            return redirect('home_view')  # or wherever you want
    else:
        form = UserCreationForm()
    return render(request, 'app1/register.html', {'form': form})    

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'app1/login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home_view')

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    
    # Only allow comment author or post author to delete
    if request.user == comment.author or request.user == comment.post.author:
        comment.delete()
    
    return redirect('post_detail', pk=post_pk)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'app1/contact.html', {'form': form})

def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=profile_user).order_by('-date')
    

    comment_count = Comment.objects.filter(author=profile_user).count()
    
    context = {
        'profile_user': profile_user,
        'posts': posts,
        'post_count': posts.count(),
        'comment_count': comment_count,
        'is_own_profile': request.user == profile_user
    }
    return render(request, 'app1/profile.html', context)




    




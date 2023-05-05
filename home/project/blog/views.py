from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Comment, Post


def signup(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      exist_user = User.objects.filter(username=username)
      if exist_user:
           error = "이미 존재하는 유저입니다."
           return render(request, 'registration/signup.html', {"error":error})
      
      new_user = User.objects.create_user(username=username, password=password)
      auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
   
      return redirect('blog:home')
       
   return render(request, 'blog/registration/signup.html')

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
          auth.login(request, user, backend="django.conrtib.auth.backends.ModelBackend")
          return redirect(request.GET.get('next', '/'))
      
      error = "아이디 또는 비밀번호가 틀립니다"
      return render(request, 'blog/registration/login.html', {"error":error})  
   return render(request, 'blog/registration/login.html')

def home(request):
   posts = Post.objects.all()

   return render(request, 'blog/home.html', {'posts':posts})


def logout(request):
   auth.logout(request)
   return redirect('blog:home')

@login_required(login_url="/registration/login/")
def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content,
           author=request.user
           )
       return redirect('detail', new_post.pk)
  
   return render(request, 'blog/new.html')

@login_required(login_url="/registration/login/")
def detail(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   
   if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        return redirect('blog:detail', post_pk);

   return render(request, 'blog/detail.html', {'post':post})


def edit(request, post_pk):
   post = Post.objects.get(pk=post_pk)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('blog:detail', post_pk)


   return render(request, 'blog/edit.html', {'post':post})


def delete(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   post.delete()
   return redirect('blog:home')


def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail', post_pk)

@login_required(login_url="/registration/login/")
def detail(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   
   if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=post,
            content=content,
            author=request.user
        )
        return redirect('detail', post_pk);

   return render(request, 'blog/detail.html', {'post':post})
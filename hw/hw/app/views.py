from .models import Post, Comment
from django.utils import timezone
from datetime import datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Comment, Post
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('deadline')
    now = datetime.now().date()
    for post in posts:
        post.days_left = (post.deadline - now).days
    complete= Post.objects.filter(cate='완료')
    notstarted= Post.objects.filter(cate='시작 안 함')
    inprogress= Post.objects.filter(cate='진행 중')

    return render(request, "home.html", {'posts': posts, 'complete': complete, 'notstarted': notstarted, 'inprogress': inprogress})

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
           cate= request.POST['cate'],
           deadline= request.POST.get('deadline'),
        )
        return redirect('home')
    return render(request, 'new.html')

def detail(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   time=Post.time
  
   if request.method == 'POST':
       content = request.POST['content']
       parent_comment_id = request.POST['parent_comment_id']
       parent_comment = Comment.objects.get(pk=parent_comment_id) if parent_comment_id else None
       Comment.objects.create(
          post = post,
          content = content,
          parent_comment = parent_comment
       )
       return redirect('detail', post.pk)
   
   return render(request, 'detail.html', {'post':post, 'time':time})


def cate(request, cate_name):
    cate_type= cate_name
    posts= Post.objects.filter(cate=cate_name)
    return render(request, "cate.html", {'cate_type': cate_type, 'cate_name':cate_name, 'posts': posts})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', post_pk)
    
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail', post_pk)

def signup(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      exist_user = User.objects.filter(username=username)
      if exist_user:
           error = "이미 존재하는 유저입니다."
           return render(request, 'registration/signup.html', {"error":error})
      
      new_user = User.objects.create_user(username=username, password=password)
      auth.login(request, new_user)
   
      return redirect('home')
       
   return render(request, 'registration/signup.html')

def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
           auth.login(request, user, backend ="django.contrib.auth.backends.ModelBackend")
           return redirect(request.GET.get('next', '/'))
      error = "아이디 또는 비밀번호가 틀립니다"
      return render(request, 'registration/login.html', {"error":error})
        
   return render(request, 'registration/login.html')

def logout(request):
   auth.logout(request)
   return redirect('home')

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
  
   return render(request, 'new.html')

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

   return render(request, 'detail.html', {'post':post})
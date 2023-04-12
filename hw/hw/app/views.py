from django.shortcuts import render, redirect
from .models import Post, Comment
from django.utils import timezone
from datetime import datetime

 


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
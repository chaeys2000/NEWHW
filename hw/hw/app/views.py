from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

# Create your views here.
timezone.now()

def home(request):
    
    hobby= Post.objects.filter(cate='취미')
    hobby_len = hobby.count()
    dog= Post.objects.filter(cate='개소리')
    dog_len = dog.count()

    diary= Post.objects.filter(cate='일기')
    diary_len = diary.count()

    posts = Post.objects.all()
    

    return render(request, "home.html", {'posts': posts, 'hobby_len' : hobby_len, 'dog_len': dog_len, 'diary_len':diary_len})

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
           cate= request.POST['cate'],
        )
        return redirect('home')
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    time = Post.time

    return render(request, 'detail.html', {'post': post, 'time': time })

def cate(request, cate_name):
    cate_type= cate_name
    posts= Post.objects.filter(cate=cate_name)
    return render(request, "cate.html", {'cate_type': cate_type, 'cate_name':cate_name, 'posts': posts})
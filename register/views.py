from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post
from commentcrud.forms import CommentForm

# Create your views here.
def write(request):
    return render(request, 'write.html')

def join2(request):
    posts = Post.objects
    return render(request, 'join2.html', {'posts': posts})

def postcreate(request):
    if request.method =='POST': # POST 방식으로 요청이 들어왔을 때
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.user = request.user
            post.save() 
            return redirect('join2') #새글 등록한 후 목록화면으로 돌아옴 
        else:
            return redirect('join2')
    else: # GET 방식으로 요청이 들어왔을 때
        form = PostForm()
        return render(request,'write.html', {'form': form})
    
def show(request, post_id):
    post = get_object_or_404(Post, pk = post_id )
    form = CommentForm()
    return render(request, 'show.html', {'post': post, 'form': form})

def postdelete(request, post_id):
    return render(request, 'join2.html')

def administration(request):
    posts = Post.objects
    qs = Post.objects.all()
    result = qs.filter(kind__icontains='Administration') # 카테고리에 경영이 포함되어 있는 레코드만 필터링
    return render(request, 'administration.html', {'posts': posts, 'result' : result})

def economy(request):
    posts = Post.objects
    qs = Post.objects.all()
    result = qs.filter(kind__icontains='Economy') # 카테고리에 경제가 포함되어 있는 레코드만 필터링
    return render(request, 'economy.html', {'posts': posts, 'result' : result})

def engineering(request):
    posts = Post.objects
    qs = Post.objects.all()
    result = qs.filter(kind__icontains='Engineering') # 카테고리에 공학이 포함되어 있는 레코드만 필터링
    return render(request, 'engineering.html', {'posts': posts, 'result' : result})

def art(request):
    posts = Post.objects
    qs = Post.objects.all()
    result = qs.filter(kind__icontains='Art') # 카테고리에 예술이 포함되어 있는 레코드만 필터링
    return render(request, 'art.html', {'posts': posts, 'result' : result})
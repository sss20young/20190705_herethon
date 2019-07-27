from django.shortcuts import render
from register.models import Post # post 모델 임포트하기
from django.contrib.auth.models import User

# Create your views here.
def mypagesee(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'mypage.html', {'posts': posts})
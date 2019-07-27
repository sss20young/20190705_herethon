from django.shortcuts import render, get_object_or_404, redirect
from register.models import Post
from .forms import CommentForm

# Create your views here.
def commentcreate(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('show', post_id=post.pk)
        

    
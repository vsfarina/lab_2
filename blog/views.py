from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post, Comment
from .forms import PostForm
from django.urls import reverse

def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment

def add_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(post=post, author=None, text=text)
            return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {'post': post})
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse('post_list'))
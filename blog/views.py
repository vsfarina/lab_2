from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post

def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save() return redirect('post_detail', pk=pk)
    return render(request,'blog/post_confirm_delete.html', {'post': post})
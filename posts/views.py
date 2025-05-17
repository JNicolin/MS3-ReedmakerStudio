from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import Post
from .forms import PostForm

## CRUD views for Post

# READ: List
def post_list(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'posts/post_list.html', {'post_list': posts})

# READ: Detail
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

# CREATE
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user 
        post.save()
        return redirect('post_list')
    return render(request, 'posts/post_form.html', {'form': form})

# UPDATE
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'posts/post_form.html', {'form': form})

# DELETE
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'components/confirm_delete.html', {
        'object_name': post.slug,
        'cancel_url': reverse('post_detail', args=[pk])
    })
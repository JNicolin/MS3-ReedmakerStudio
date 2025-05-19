from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from .forms import PostForm
from comments.forms import CommentForm

# READ: List
def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, "posts/post_list.html", {
        "posts": posts
    })

# READ: Detail with comments
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated and request.POST.get("submit_comment"):
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.content_object = post
                comment.save()
                return redirect('post_detail', pk=pk)
        else:
            return redirect('account_login')

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

# CREATE
@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user 
        post.save()
        return redirect('post_list')
    return render(request, 'posts/post_form.html', {'form': form})

# UPDATE
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=pk)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'posts/post_form.html', {'form': form})

# DELETE
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'components/confirm_delete.html', {
        'object_name': post.slug,
        'cancel_url': reverse('post_detail', args=[pk])
    })

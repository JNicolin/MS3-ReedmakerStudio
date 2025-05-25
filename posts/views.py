from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from .forms import PostForm
from comments.forms import CommentForm

# Route for home page html
def home(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    return render(request, "home.html", {"posts": posts})

# READ: List posts
def post_list(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')

    # User log-in required to post 
    form = PostForm(request.POST or None) if request.user.is_authenticated else None

    if request.method == "POST" and request.user.is_authenticated:
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')

    return render(request, "posts/post_list.html", {
        "posts": posts,
        "form": form,
    })

# READ: Read detail of a post, or add a comment
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

# CREATE a post, autosave the current user as owner
@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user 
        post.save()
        return redirect('post_list')
    return render(request, 'components/_object_form.html', {
        "form": form,
        "title": "Add a blog post",
        "cancel_url": reverse("reed_list")
    })

# UPDATE a post, if the user is the owner
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=pk)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'components/_object_form.html', {
        "form": form,
        "title": "Update a blog post",
        "cancel_url": reverse("reed_list")
    })

# DELETE a post, if the user is the owner
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
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Reed
from .forms import ReedForm

# CRUD views for Reed

# READ: List
def reed_list(request):
    posts = Reed.objects.all().order_by('-created_on')
    return render(request, 'reeds/reed_list.html', {'reed_list': reeds})

# READ: Detail
def reed_detail(request, pk):
    post = get_object_or_404(Reed, pk=pk)
    return render(request, 'reeds/reed_detail.html', {'reed': reed})

# CREATE
def reed_create(request):
    form = ReedForm(request.POST or None)
    if form.is_valid():
        reed = form.save(commit=False)
        reed.author = request.user 
        reed.save()
        return redirect('reed_list')
    return render(request, 'reeds/reed_form.html', {'form': form})

# UPDATE
def reed_update(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    reed = ReedForm(request.POST or None, instance=reed)
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
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

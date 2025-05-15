from django.shortcuts import render, get_object_or_404, redirect
from .models import Reed
from .forms import ReedForm
from comments.forms import CommentForm

# CRUD views for Reed

# READ: List
def reed_list(request):
    posts = Reed.objects.all().order_by('-created_on')
    return render(request, 'reeds/reed_list.html', {'reeds': reeds})

# READ: Detail
def reed_detail(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    comments = reed.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.content_object = reed
            comment.save()
            return redirect('reed_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'reeds/reed_detail.html', {
        'reed': reed,
        'comments': comments,
        'form': form
    })

# CREATE
def reed_create(request):
    form = ReedForm(request.POST or None)
    if form.is_valid():
        reed = form.save(commit=False)
        reed.item_creator = request.user 
        reed.save()
        return redirect('reed_list')
    return render(request, 'reeds/reed_form.html', {'form': form})

# UPDATE
def reed_update(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    form = ReedForm(request.POST or None, instance=reed)
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=pk)
    return render(request, 'reeds/reed_form.html', {'form': form})

# DELETE
def reed_delete(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    if request.method == 'POST':
        reed.delete()
        return redirect('reed_list')
    return render(request, 'posts/post_confirm_delete.html', {'reed': reed})

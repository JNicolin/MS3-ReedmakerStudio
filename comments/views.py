from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Comment
from .forms import CommentForm

## CRUD views for comments, where Read only happens via the reeds/views.py as part of the reed_detail

@login_required
def comment_create(request, content_type_id, object_id):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.content_type_id = content_type_id
        comment.object_id = object_id
        comment.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'components/_object_form.html', {
        'form': form,
        'title': 'Add Comment',
        'cancel_url': request.META.get('HTTP_REFERER', '/')
    })

@login_required
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'components/_object_form.html', {
        'form': form,
        'title': 'Edit Comment',
        'cancel_url': request.META.get('HTTP_REFERER', '/')
    })

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'components/confirm_delete.html', {
        'object_name': comment.title,
        'cancel_url': request.META.get('HTTP_REFERER', '/')
    })
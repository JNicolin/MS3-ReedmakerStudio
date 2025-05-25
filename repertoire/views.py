from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Repertoire
from .forms import RepertoireForm
from reeds.models import Reed

## CRUD views for comments, where Read only happens via the reeds/views.py as part of the reed_detail

@login_required
def repertoire_create(request, reed_pk):
    reed = get_object_or_404(Reed, pk=reed_pk)
    form = RepertoireForm(request.POST or None, initial={'reed': reed})
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=reed.pk)
    return render(request, 'components/_object_form.html', {
        'form': form,
        'title': 'Add Repertoire',
        'cancel_url': reverse('reed_detail', args=[reed.pk])
    })

@login_required
def repertoire_update(request, pk):
    repertoire = get_object_or_404(Repertoire, pk=pk)
    form = RepertoireForm(request.POST or None, instance=repertoire)
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=repertoire.reed.pk)
    return render(request, 'components/_object_form.html', {
        'form': form,
        'title': 'Edit Repertoire',
        'cancel_url': reverse('reed_detail', args=[repertoire.reed.pk])
    })

@login_required
def repertoire_delete(request, pk):
    repertoire = get_object_or_404(Repertoire, pk=pk)
    if request.method == 'POST':
        repertoire.delete()
        return redirect('reed_detail', pk=repertoire.reed.pk)
    return render(request, 'components/confirm_delete.html', {
        'object_name': repertoire.music_title,
        'cancel_url': reverse('reed_detail', args=[repertoire.reed.pk])
    })

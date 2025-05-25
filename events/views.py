from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Event
from .forms import EventForm
from reeds.models import Reed

## CRUD views for comments, where Read only happens via the reeds/views.py as part of the reed_detail

@login_required
def event_create(request, reed_pk):
    reed = get_object_or_404(Reed, pk=reed_pk)
    form = EventForm(request.POST or None, initial={'reed': reed})
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=reed.pk)
    return render(request, 'components/_object_form.html', {
        'form': form,
        'title': 'Add Event',
        'cancel_url': reverse('reed_detail', args=[reed.pk])
    })

@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=event.reed.pk)
    return render(request, 'components/_object_form.html', {
        'form': form,
        'title': 'Edit Event',
        'cancel_url': reverse('reed_detail', args=[event.reed.pk])
    })

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('reed_detail', pk=event.reed.pk)
    return render(request, 'components/confirm_delete.html', {
        'object_name': event.gig_title,
        'cancel_url': reverse('reed_detail', args=[event.reed.pk])
    })

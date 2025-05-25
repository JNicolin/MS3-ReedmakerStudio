from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Reed
from .choices import Rating, Instrument
from .forms import ReedForm

## CRUD views for Reed

# READ: List all reeds
def reed_list(request):
    reeds = Reed.objects.all()
    selected_instrument = request.GET.get("instrument")
    selected_sort = request.GET.get("sort")

    if selected_instrument:
        reeds = reeds.filter(item_type=selected_instrument)
    if selected_sort:
        reeds = reeds.order_by(selected_sort)
    else:
        reeds = reeds.order_by('-created_on')

    return render(request, "reeds/reed_list.html", {
        "reeds": reeds,
        "Instrument": Instrument,
        "selected_instrument": selected_instrument,
        "selected_sort": selected_sort,
    })

# READ: Read details about a selected reed, including associated events/repertoire/comments
def reed_detail(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    comments = reed.comments.all()
    events = reed.targeted_gigs.all()
    repertoire = reed.repertoire_list.all()

    return render(request, 'reeds/reed_detail.html', {
        'reed': reed,
        'comments': comments,
        'events': events,
        'repertoire': repertoire,
    })

# CREATE a new reed
@login_required
def reed_create(request):
    form = ReedForm(request.POST or None)
    if form.is_valid():
        reed = form.save(commit=False)
        reed.item_creator = request.user 
        reed.save()
        return redirect('reed_list')
    return render(request, 'components/_object_form.html', {
        "form": form,
        "title": "Create Reed",
        "cancel_url": reverse("reed_list")
})

# UPDATE an existing reed
@login_required
def reed_update(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    if request.user != reed.item_creator:
        return redirect('reed_detail', pk=pk)

    form = ReedForm(request.POST or None, instance=reed)
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=pk)
    return render(request, 'components/_object_form.html', {
        "form": form,
        "title": "Update Reed ",
        "cancel_url": reverse("reed_detail", args=[pk])
})

# DELETE a selected reed
@login_required
def reed_delete(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    # check if logged in user is the owner
    if request.user != reed.item_creator:
        return redirect('reed_detail', pk=pk)

    # if POST request 
    if request.method == 'POST':
        reed.delete()
        return redirect('reed_list')

    # if GET request (delete not yet confirmed)
    return render(request, 'components/confirm_delete.html', {
        'object_name': reed.item_id,
        'cancel_url': reverse('reed_detail', args=[pk])
    })
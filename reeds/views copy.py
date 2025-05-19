from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Reed
from .choices import Rating, Instrument
from .forms import ReedForm
from comments.forms import CommentForm

# Route for the home view
def home(request):
    return render(request, 'home.html')

## CRUD views for Reed

# READ: List
def reed_list(request):
    reeds = Reed.objects.all()
    selected_instrument = request.GET.get("instrument")
    selected_rating = request.GET.get("rating")
    selected_sort = request.GET.get("sort")
    only_mine = request.GET.get("mine") == "1"

    if only_mine and request.user.is_authenticated:
        reeds = reeds.filter(item_creator=request.user)

    if selected_instrument:
        reeds = reeds.filter(item_type=selected_instrument)
    if selected_rating:
        reeds = reeds.filter(item_rating=selected_rating)
    if selected_sort:
        reeds = reeds.order_by(selected_sort)
    else:
        reeds = reeds.order_by('-created_on')

    return render(request, "reeds/reed_list.html", {
        "reeds": reeds,
        "Instrument": Instrument,
        "Rating": Rating,
        "selected_instrument": selected_instrument,
        "selected_rating": selected_rating,
        "selected_sort": selected_sort,
        "only_mine": only_mine,
    })

# READ: Detail
def reed_detail(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    comments = reed.comments.all()
    events = reed.targeted_gigs.all()
    repertoire = reed.repertoire_list.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.content_object = reed
                comment.save()
                return redirect('reed_detail', pk=pk)
        else:
            return redirect('account_login')
    else:
        form = CommentForm()

    return render(request, 'reeds/reed_detail.html', {
        'reed': reed,
        'comments': comments,
        'form': form,
        'events': events,
        'repertoire': repertoire,
    })

# CREATE
@login_required
def reed_create(request):
    form = ReedForm(request.POST or None)
    if form.is_valid():
        reed = form.save(commit=False)
        reed.item_creator = request.user 
        reed.save()
        return redirect('reed_list')
    return render(request, 'reeds/reed_form.html', {'form': form})

# UPDATE
@login_required
def reed_update(request, pk):
    reed = get_object_or_404(Reed, pk=pk)
    if request.user != reed.item_creator:
        return redirect('reed_detail', pk=pk)

    form = ReedForm(request.POST or None, instance=reed)
    if form.is_valid():
        form.save()
        return redirect('reed_detail', pk=pk)
    return render(request, 'reeds/reed_form.html', {'form': form})

# DELETE
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
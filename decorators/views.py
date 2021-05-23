from typing import Reversible
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from decorators.models import Entry
from decorators.forms import EntryForm

from decorators.decorator import user_is_entry_author, superuser_only, timeit

from django.contrib.auth.models import User

@login_required
def index(request):
    entries = Entry.objects.filter(created_by=request.user)
    return render(request, 'index.html', { 'entries': entries })

@login_required
@timeit
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry was successfully added!')
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'entry.html', { 'form': form })

@login_required
@user_is_entry_author
def edit(request, id):
    entry = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry was successfully edited!')
            return redirect('index')
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entry.html', { 'form': form })

@login_required
@user_is_entry_author
def remove(request, id):
    entry = get_object_or_404(Entry, pk=id)
    entry.delete()
    messages.success(request, 'Entry was successfully removed!')
    return redirect('index')

@login_required
@user_is_entry_author
@superuser_only
def transfer(request, id):
    entry = get_object_or_404(Entry, pk=id)
    print(request.POST)
    if request.method == 'POST':
        transfer = request.POST.get('transfer_to')
        new_user = User.objects.get(username=transfer)
        entry.created_by = new_user
        entry.save()
        return redirect('index')

    return render(request, 'transfer.html', context = {'entry': entry})

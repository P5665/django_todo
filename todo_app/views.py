from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()

            messages.success(request, ('Another thing added to your plate! Bring it on!!'))
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    context = {'first_name': 'Ben', 'last_name': 'Peterson'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()

    messages.success(request, ('To-Do item has been removed!'))
    return redirect('td1_home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True

    item.save()

    messages.success(request, ('Way to go! You successfully completed: ' + item.item))
    return redirect('td1_home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False

    item.save()
    return redirect('td1_home')

def edit(request, list_id):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()

            messages.success(request, ('Item has been edited!!'))
            all_items = List.objects.all
            return render(request, 'edit.html', {'all_items': all_items})

    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})
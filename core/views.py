from django.shortcuts import render, redirect, get_object_or_404
from .models import client
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm


# Create your views here.

@login_required
def crm_index(request):
    return render(request, 'index.html')

@login_required
def client_detail(request, pk):
    person = get_object_or_404(client, pk=pk)
    return render(request, 'index.html', {'person': person})

@login_required
def client_add(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'client_add.html', {
        'form': form
    })

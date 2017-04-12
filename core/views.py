from django.shortcuts import render, redirect, get_object_or_404
from .models import client, work, Photo
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm, WorkForm, PhotoForm
from django.http import JsonResponse
from django.views import View


# Create your views here.

@login_required
def crm_index(request):
    return render(request, 'index.html')

@login_required
def client_list(request):
    clients = client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    person = get_object_or_404(client, pk=pk)
    return render(request, 'client_detail.html', {'person': person})

@login_required
def client_add(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'client_add.html', {'form': form})

@login_required
def client_edit(request, pk):
    person = get_object_or_404(client, pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('client_detail', pk=person.pk)
    else:
        form = DocumentForm(instance=person)
    return render(request, 'client_add.html', {'form': form})

@login_required
def work_list(request):
    works = work.objects.all()
    return render(request, 'work_list.html', {'works': works})

@login_required
def work_detail(request, pk):
    done = get_object_or_404(work, pk=pk)
    photos = work.objects.filter()
    return render(request, 'work_detail.html', {'done': done})

@login_required
def work_add(request):
    clients = client.objects.all()
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WorkForm()
    return render(request, 'work_add.html', {'form': form, 'clients': clients})

@login_required
def work_edit(request, pk):
    done = get_object_or_404(work, pk=pk)
    if request.method == "POST":
        form = WorkForm(request.POST, request.FILES, instance=done)
        if form.is_valid():
            done = form.save(commit=False)
            done.save()
            return redirect('work_detail', pk=done.pk)
    else:
        form = WorkForm(instance=done)
    return render(request, 'work_add.html', {'form': form})

class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/test.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.title = 'blabla_new'
            photo.client_id = 1
            photo.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

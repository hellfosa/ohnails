from django.shortcuts import render, redirect, get_object_or_404
from .models import client, work, Photo
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm, WorkForm


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
    photos = Photo.objects.filter(client_name=done.client, uploaded_at=done.date)
    if request.method == 'GET':
        return render(request, 'work_detail.html', {'done': done, 'photos': photos})
    elif request.method == 'POST':
        photo = Photo.objects.get(photo_uuid=request.POST.get('uuid'))
        Photo.publish_switch(photo)
        if photo.published == True:
            publ_status = 1
        else:
            publ_status = 0
        photo.save()
        return render(request, 'work_detail.html', {'done': done, 'photos': photos, 'publ_status': publ_status})


@login_required
def work_add(request):
    clients = client.objects.all()
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        files = request.FILES.getlist('photo')
        if form.is_valid():
            for file in files:
                obj = Photo(client_name=form.cleaned_data['client'], file=file)
                print(form.cleaned_data['client'])
                obj.save()
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
        files = request.FILES.getlist('photo')
        if form.is_valid():
            for file in files:
                obj = Photo(client_name=done.client, file=file)
                obj.save()
            done = form.save(commit=False)
            done.save()
            return redirect('work_detail', pk=done.pk)
    else:
        form = WorkForm(instance=done)
    return render(request, 'work_add.html', {'form': form})

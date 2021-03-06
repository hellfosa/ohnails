from django.shortcuts import render, redirect, get_object_or_404
from .models import client, work, Photo, work_categorie
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm, WorkForm, Contact
from django.core.mail import send_mail


# Create your views here.

@login_required
def crm_index(request):
    if request.method == 'GET':
        works = work.objects.all().order_by('date')[:5]
        print(works)
        return render(request, 'index.html', {'works': works})

@login_required
def client_list(request):
    if request.method == 'GET':
        clients = client.objects.all()
        return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    if request.method == 'GET':
        person = get_object_or_404(client, pk=pk)
        works = work.objects.filter(client=person)[:5]
        return render(request, 'client_detail.html', {'person': person, 'client_works': works})

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
    photos = Photo.objects.filter(client_name=done.client, uploaded_at=done.date, category=done.work_category)
    if request.method == 'GET':
        return render(request, 'work_detail.html', {'done': done, 'photos': photos})
    elif request.method == 'POST' and request.POST.get('remove') != 'True':
        photo = Photo.objects.get(photo_uuid=request.POST.get('uuid'))
        Photo.publish_switch(photo)
        if photo.published == True:
            publ_status = 1
        else:
            publ_status = 0
        photo.save()
        return render(request, 'work_detail.html', {'done': done, 'photos': photos, 'publ_status': publ_status})
    elif request.method == 'POST' and request.POST.get('remove') == 'True':
        photo = Photo.objects.get(photo_uuid=request.POST.get('uuid'))
        Photo.remove_photo(photo)
        if photo.published == True:
            publ_status = 1
        else:
            publ_status = 0
        return render(request, 'work_detail.html', {'done': done, 'photos': photos, 'publ_status': publ_status})

@login_required
def work_add(request):
    clients = client.objects.all()
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        files = request.FILES.getlist('photo')
        if form.is_valid():
            for file in files:
                obj = Photo(client_name=form.cleaned_data['client'], category=form.cleaned_data['work_category'], file=file, uploaded_at=form.cleaned_data['date'])
                print(form.cleaned_data['client'])
                obj.save()
            form.save()
            return redirect('/main')
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
            print(form.cleaned_data['date'])
            for file in files:
                obj = Photo(client_name=done.client, file=file)
                obj.save()
            done = form.save(commit=False)
            done.save()
            return redirect('work_detail', pk=done.pk)
    else:
        form = WorkForm(instance=done)
    return render(request, 'work_add.html', {'form': form})


def public_index(request):
    form = Contact(request.POST)
    categories = work_categorie.objects.all()
    works = work.objects.all()
    photos = Photo.objects.all()
    work_cats = {}
    for category in categories:
        work_cats[category.category] = photos.filter(published=True).filter(category=category).order_by('uploaded_at')[:15]
    if request.method == 'POST':
        print(request.POST)
        message = '''\
        У вас новая заявка на маникюр
    \
        Имя - {0}
    \
        Телефон - {1}
    \
        Текст сообщения:
    \
        {2}
        '''.format(request.POST.get('name'), request.POST.get('mobile'), request.POST.get('message'))
        send_mail('Работать негры!', message, 'info@oh-nails.ru', ['info@oh-nails.ru'])
    return render(request, 'public/index.html', {'categories': categories, 'works': works, 'work_cats': work_cats, 'form': form})

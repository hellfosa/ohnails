from django import forms
from django.utils import timezone
from .models import client, work, Photo, work_categorie
from django.conf import settings
from django.forms.formsets import formset_factory



class DocumentForm(forms.ModelForm):
    class Meta:
        model = client
        exclude = ()
    fio = forms.CharField(label='ФИО клиента')
    birth_date = forms.DateField(label='День рождения', input_formats=settings.DATE_INPUT_FORMATS)
    last_work = forms.DateField(label='Дата последнего визита', initial=timezone.now, input_formats=settings.DATE_INPUT_FORMATS)
    email = forms.EmailField(label='Эл. почта')
    mobile = forms.CharField(label='Мобильный')
    contra = forms.CharField(label='Противопоказания')
    additional = forms.CharField(label='Примечания')
    pros = forms.IntegerField(label='Переплата', initial=0)
    cons = forms.IntegerField(label='Задолженность', initial=0)
    photo = forms.FileField(label='Фотография клиента')

class WorkForm(forms.ModelForm):
    class Meta:
        model = work
        exclude = ()
    client = forms.ModelChoiceField(label='Имя клиента', queryset=client.objects.all(), empty_label='Выбери клиента!')
    work_category = forms.ModelChoiceField(label='Категория', queryset=work_categorie.objects.all(), empty_label='Выбери категорию')
    date = forms.DateField(label='Дата работы', initial=timezone.now, input_formats=settings.DATE_INPUT_FORMATS)
    cost = forms.IntegerField(help_text='Стоимость работы')
    photo = forms.FileField(label='Фото работы', widget=forms.ClearableFileInput(attrs={'multiple': True}))


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)
    uploaded_at = forms.DateField(label='Дата работы', initial=timezone.now, input_formats=settings.DATE_INPUT_FORMATS)

class Contact(forms.Form):
    client = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    mobile = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон для связи'}))
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сообщение'}))

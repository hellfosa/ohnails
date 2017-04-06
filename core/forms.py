from django import forms
from django.utils import timezone
from .models import client
from bootstrap3_datepicker.fields import DatePickerField
from bootstrap3_datepicker.widgets import DatePickerInput

class DocumentForm(forms.Form):

    fio = forms.CharField(label='ФИО клиента')
    birth_date = forms.DateField(widget=DatePickerInput())
    last_work = forms.DateField(widget=DatePickerInput(format="%Y-%m-%d"))
    email = forms.EmailField(label='Эл. почта')
    mobile = forms.CharField(label='Мобильный')
    contra = forms.CharField(label='Противопоказания')
    additional = forms.CharField(label='Примечания')
    pros = forms.IntegerField(label='Переплата', initial=0)
    cons = forms.IntegerField(label='Задолженность', initial=0)
    photo = forms.FileField(label='Фотография клиента')


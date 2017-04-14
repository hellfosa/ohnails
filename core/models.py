from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class client(models.Model):
    fio = models.CharField(max_length=300, default='Введи ФИО тут')
    birth_date = models.DateField(default=timezone.now)
    last_work = models.DateField(default=timezone.now)
    email = models.EmailField(default='Почту@тут.введи')
    mobile = models.CharField(max_length=10, default='Мобильник')
    contra = models.TextField(default='Противопоказания')
    pros = models.IntegerField(default=0)
    cons = models.IntegerField(default=0)
    additional = models.TextField(default='Всякие примечания')
    photo = models.FileField(upload_to='peoples/')


    def __str__(self):
        return self.fio

class work(models.Model):
    work_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date = models.DateField(auto_now_add=True)
    cost = models.IntegerField(default=0)
    photo = models.FilePathField(path='works/%Y/%m/%d')
    category = models.CharField(max_length=100, blank=True)
    client = models.CharField(max_length=300, default='Выбери клиента')

    def __str__(self):
        return '{0}-{1}'.format(self.client, self.date)

class Photo(models.Model):
    photo_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    client_name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True)
    uploaded_at = models.DateField(auto_now_add=True)

    def publish_switch(self):
        if self.published == True:
            self.published = False
        else:
            self.published = True

    def __str__(self):
        return '{0}-{1}'.format(self.client_name, self.uploaded_at)
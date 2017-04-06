from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


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

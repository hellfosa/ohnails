from django.contrib import admin
from .models import client, work, Photo, work_categorie

# Register your models here.
admin.site.register(client)
admin.site.register(work_categorie)
admin.site.register(work)
admin.site.register(Photo)
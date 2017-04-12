from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.crm_index, name='crm_index'),
    url(r'^clients/$', views.client_list, name='client_list'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    url(r'^client_add/$', views.client_add, name='client_add'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^works/$', views.work_list, name='work_list'),
    url(r'^work/(?P<pk>[0-9]+)/$', views.work_detail, name='work_detail'),
    url(r'^work_add/$', views.work_add, name='work_add'),
    url(r'^work/(?P<pk>[0-9]+)/edit/$', views.work_edit, name='work_edit'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
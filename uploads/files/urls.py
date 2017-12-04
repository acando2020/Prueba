from django.conf.urls import url
from files.models import Document
from files.views import upload_file,DocumentoList,DocumentoUpdate

urlpatterns = [

    url(r'^cargar$',upload_file, name="cargar"),
    url(r'^lista$',DocumentoList.as_view(), name="lista"),
    url(r'^update/(?P<pk>\d+)/$',DocumentoUpdate.as_view(), name="actualizar"),

]
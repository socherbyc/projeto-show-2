from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gvectors_index'),
    path('gvectors/create', views.create, name='gvectors_create'),
    path('gvectors/<int:gvector_id>', views.show, name='gvectors_show'),
    path('gvectors/<int:gvector_id>.json', views.show_json, name='gvectors_show_json'),
    path('gvectors/process/<int:gvector_id>', views.process, name='gvectors_process'),
    path('gvectors/delete/<int:gvector_id>', views.delete, name='gvectors_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
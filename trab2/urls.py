
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gvectors.urls'), name="gvectors"),
    path('admin/', admin.site.urls),
]

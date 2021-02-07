from django.contrib import admin
from django.urls import path, include
from leads._main import init
from leads.views import _redirect 


init()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/', include(('leads.urls', 'leads'), namespace='leads')),
    path('',_redirect)
]
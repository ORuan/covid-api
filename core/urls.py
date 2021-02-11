from django.contrib import admin
from django.urls import path, include
from leads._main import init
from leads.views import _redirect, qr_code
from django.conf import settings
from django.conf.urls.static import static
init()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('u/', include(('leads.urls', 'leads'), namespace='leads')),
    path('8ade7b25-d7c9-400c-8ea6-e1c8413d01af/', qr_code),
    path('',_redirect)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
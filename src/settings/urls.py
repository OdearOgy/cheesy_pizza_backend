
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)






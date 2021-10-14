from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('store/', include(('store.urls', 'store'), namespace='store')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

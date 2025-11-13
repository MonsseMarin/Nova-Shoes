from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),           # Página principal
    path('catalogo/', include('catalogo.urls')),
    path('usuarios/', include('usuarios.urls')),   
    path('carrito/', include('carrito.urls')),
    path('feedback/', include('feedback.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
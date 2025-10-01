# barbearia/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # Painel administrativo do Django
    path("admin/", admin.site.urls),

    # URLs do app principal "agenda"
    path("agenda/", include(("agenda.urls", "agenda"), namespace="agenda")),

    # Redireciona a raiz '/' para '/agenda/'
    path("", lambda request: redirect("agenda/")),
]

# Servir arquivos de mídia e estáticos (somente durante desenvolvimento)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

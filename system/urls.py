from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panelės URL
    path('', include('blog.urls', namespace='blog')),  # Pagrindinės tinklalapio URL
    path('users/', include('users.urls', namespace='users')),  # Vartotojų valdymo URL
    path('tinymce/', include('tinymce.urls')),  # TinyMCE redaktoriaus URL
]

# Papildomi URL, kai debug režimas yra įjungtas
if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

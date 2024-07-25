from django.urls import path
from .views import index, post, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:pk>/',post, name='post'),
    path('contact/', contact, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
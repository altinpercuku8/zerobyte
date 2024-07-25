from django.urls import path
from .views import threads, delete_thread
urlpatterns = [
    path('', threads, name='threads'),
    path('delete/<int:pk>', delete_thread, name='delete')
]
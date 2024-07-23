from django.urls import path
from .views import threads
urlpatterns = [
    path('', threads, name='threads'),
]
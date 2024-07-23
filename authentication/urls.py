from django.urls import path
from .views import login_user, register, log_out
urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('log_out/', log_out, name='logout'),
]
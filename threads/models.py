from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Thread(models.Model):
    thread_title = models.CharField(max_length=255)
    thread_content = models.TextField()
    thread_author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thread_title
